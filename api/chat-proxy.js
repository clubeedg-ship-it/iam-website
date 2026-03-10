// Simple Express proxy for OpenRouter chat API
// Keeps API key server-side, rate-limits clients
require('dotenv').config();
const express = require('express');
const cors = require('cors');
const rateLimit = require('express-rate-limit');

const app = express();
const PORT = process.env.CHAT_PROXY_PORT || 3860;
const API_KEY = process.env.OPENROUTER_API_KEY;
const MODEL = process.env.CHAT_MODEL || 'qwen/qwen3.5-397b-a17b';

if (!API_KEY) {
  console.error('OPENROUTER_API_KEY env var required');
  process.exit(1);
}

app.use(cors({ origin: /interactivemove\.nl$/ }));
app.use(express.json({ limit: '16kb' }));

// Rate limit: 20 requests per minute per IP
const limiter = rateLimit({
  windowMs: 60 * 1000,
  max: 20,
  message: { error: 'Too many requests, try again later' }
});
app.use('/chat', limiter);

app.post('/chat', async (req, res) => {
  const { messages } = req.body;
  if (!Array.isArray(messages) || messages.length === 0 || messages.length > 30) {
    return res.status(400).json({ error: 'Invalid messages' });
  }

  // Sanitize: only allow role user/assistant/system, string content
  const clean = messages.filter(m =>
    ['user', 'assistant', 'system'].includes(m.role) &&
    typeof m.content === 'string' &&
    m.content.length < 4000
  );

  try {
    const response = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${API_KEY}`,
        'Content-Type': 'application/json',
        'HTTP-Referer': 'https://interactivemove.nl',
        'X-Title': 'IAM Support Chat'
      },
      body: JSON.stringify({
        model: MODEL,
        messages: clean,
        stream: true,
        max_tokens: 1024
      })
    });

    if (!response.ok) {
      const err = await response.text();
      return res.status(502).json({ error: 'Upstream error', status: response.status });
    }

    // Stream SSE through to client
    res.setHeader('Content-Type', 'text/event-stream');
    res.setHeader('Cache-Control', 'no-cache');
    res.setHeader('Connection', 'keep-alive');

    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      res.write(decoder.decode(value, { stream: true }));
    }
    res.end();
  } catch (err) {
    console.error('Proxy error:', err.message);
    res.status(500).json({ error: 'Internal error' });
  }
});

app.listen(PORT, '127.0.0.1', () => {
  console.log(`Chat proxy on :${PORT}`);
});
