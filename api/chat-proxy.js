// Simple Proxy for OpenRouter chat API
// Standalone version (no Express)
const http = require('http');
const https = require('https');

const PORT = process.env.CHAT_PORT || 3860;
const API_KEY = process.env.OPENROUTER_API_KEY;
const MODEL = process.env.CHAT_MODEL || 'google/gemini-2.0-flash-001';

if (!API_KEY) {
  console.warn('OPENROUTER_API_KEY not set — chat proxy disabled');
}

const server = http.createServer((req, res) => {
  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    return res.end();
  }

  if (req.method === 'POST' && req.url === '/chat') {
    let body = '';
    req.on('data', chunk => { body += chunk; });
    req.on('end', () => {
      try {
        const { messages } = JSON.parse(body);
        
        const postData = JSON.stringify({
          model: MODEL,
          messages: messages,
          stream: true
        });

        const options = {
          hostname: 'openrouter.ai',
          path: '/api/v1/chat/completions',
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${API_KEY}`,
            'Content-Type': 'application/json',
            'X-Title': 'IAM Support Chat'
          }
        };

        const proxyReq = https.request(options, (proxyRes) => {
          res.writeHead(proxyRes.statusCode, proxyRes.headers);
          proxyRes.pipe(res);
        });

        proxyReq.on('error', (err) => {
          console.error(err);
          res.writeHead(500);
          res.end('Proxy Error');
        });

        proxyReq.write(postData);
        proxyReq.end();

      } catch (e) {
        res.writeHead(400);
        res.end('Invalid JSON');
      }
    });
  } else {
    res.writeHead(404);
    res.end('Not Found');
  }
});

server.listen(PORT, () => {
  console.log(`Chat proxy running on port ${PORT}`);
});
