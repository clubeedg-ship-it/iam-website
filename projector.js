/**
 * Interactive Floor Projector Simulation
 * 
 * A minimalist particle physics engine simulating a motion-reactive floor.
 * Designed for HTMX compatibility and performance.
 */

class InteractiveFloor {
    constructor() {
        this.canvas = document.getElementById('projector-canvas');
        if (!this.canvas) return;

        this.ctx = this.canvas.getContext('2d');
        this.particles = [];
        this.animationId = null;
        this.width = 0;
        this.height = 0;

        // Config
        this.particleCount = 25; // Reduced for subtler effect
        this.connectionDistance = 200; // Increased for massive particles
        this.mouseRadius = 300; // Huge interaction zone
        this.baseSpeed = 0.5;

        // Interaction State
        this.mouse = { x: null, y: null, isActive: false };

        // Bind methods
        this.resize = this.resize.bind(this);
        this.animate = this.animate.bind(this);
        this.handleMove = this.handleMove.bind(this);
        this.handleLeave = this.handleLeave.bind(this);

        this.init();
    }

    init() {
        this.resize();
        this.createParticles();
        this.addListeners();
        this.animate();
    }

    destroy() {
        cancelAnimationFrame(this.animationId);
        window.removeEventListener('resize', this.resize);
        window.removeEventListener('mousemove', this.handleMove);
        window.removeEventListener('touchmove', this.handleMove);
        // We can keep leave/end on window too for consistency
        window.removeEventListener('mouseout', this.handleLeave);
        window.removeEventListener('touchend', this.handleLeave);
    }

    addListeners() {
        window.addEventListener('resize', this.resize);

        // Mouse - Listen on WINDOW to capture events through glass panels
        window.addEventListener('mousemove', this.handleMove);
        window.addEventListener('mouseout', this.handleLeave);

        // Touch - Listen on WINDOW
        window.addEventListener('touchmove', (e) => {
            // Only prevent default if touching background? 
            // Actually, for full screen effect, we might want to allow scroll 
            // BUT user wants interaction. Let's leave default behavior (scroll) 
            // but capture coordinates.
            // e.preventDefault(); 
            this.handleMove(e.touches[0]);
        }, { passive: true });

        window.addEventListener('touchend', this.handleLeave);
    }

    resize() {
        // Fullscreen Fixed Canvas
        this.width = window.innerWidth;
        this.height = window.innerHeight;

        // Handle DPI
        const dpr = window.devicePixelRatio || 1;
        this.canvas.width = this.width * dpr;
        this.canvas.height = this.height * dpr;
        this.ctx.scale(dpr, dpr);

        // Re-distribute particles if dimension changes significantly
        if (this.particles.length === 0) this.createParticles();
    }

    createParticles() {
        this.particles = [];
        // Industrial Palette: Red, Yellow, Dark Greys
        const colors = ['#d23234', '#feba04', '#333333', '#4d4d4d', '#2a2a2a'];

        for (let i = 0; i < this.particleCount; i++) {
            this.particles.push({
                x: Math.random() * this.width,
                y: Math.random() * this.height,
                vx: (Math.random() - 0.5) * this.baseSpeed,
                vy: (Math.random() - 0.5) * this.baseSpeed,
                size: Math.random() * 30 + 15, // Smaller particles (15px to 45px radius)
                color: colors[Math.floor(Math.random() * colors.length)],
                baseX: Math.random() * this.width,
                baseY: Math.random() * this.height
            });
        }
    }

    handleMove(e) {
        // Since canvas is fixed fullscreen (0,0), clientX/Y are the coords
        this.mouse.x = e.clientX;
        this.mouse.y = e.clientY;
        this.mouse.isActive = true;
    }

    handleLeave() {
        this.mouse.x = null;
        this.mouse.y = null;
        this.mouse.isActive = false;
    }

    animate() {
        // Trail effect: Draw semi-transparent rectangle instead of clearRect
        this.ctx.fillStyle = 'rgba(240, 244, 248, 0.3)'; // Increased opacity slightly to clean trails faster
        this.ctx.fillRect(0, 0, this.width, this.height);

        // Update and Draw Particles
        for (let i = 0; i < this.particles.length; i++) {
            let p = this.particles[i];

            // 1. Physics: Brownian Motion (Base Movement)
            p.x += p.vx;
            p.y += p.vy;

            // 2. Physics: Interaction (Repulsion/Flow)
            if (this.mouse.isActive) {
                let dx = this.mouse.x - p.x;
                let dy = this.mouse.y - p.y;
                let distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < this.mouseRadius) {
                    // Calculate force vector
                    const forceDirectionX = dx / distance;
                    const forceDirectionY = dy / distance;
                    const force = (this.mouseRadius - distance) / this.mouseRadius;

                    // Repel strength
                    const strength = 3;
                    const directionX = forceDirectionX * force * strength;
                    const directionY = forceDirectionY * force * strength;

                    p.vx -= directionX;
                    p.vy -= directionY;
                }
            }

            // 3. Friction (Slow down high velocities)
            // If velocity is high, apply stronger friction to return to calm state
            const currentSpeed = Math.sqrt(p.vx * p.vx + p.vy * p.vy);
            if (currentSpeed > this.baseSpeed) {
                p.vx *= 0.95;
                p.vy *= 0.95;
            } else {
                // Keep them moving a little bit always
                if (Math.abs(p.vx) < 0.1) p.vx += (Math.random() - 0.5) * 0.05;
                if (Math.abs(p.vy) < 0.1) p.vy += (Math.random() - 0.5) * 0.05;
            }

            // 4. Bounds Checking (Wrap around)
            if (p.x > this.width) p.x = 0;
            else if (p.x < 0) p.x = this.width;
            if (p.y > this.height) p.y = 0;
            else if (p.y < 0) p.y = this.height;

            // 5. Draw Particle
            this.ctx.beginPath();
            this.ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            this.ctx.fillStyle = p.color;

            // Removed shadowBlur and lighter composite for better visibility/performance on light bg

            this.ctx.fill();
        }

        // Optional: Connect particles (Constellation effect) - subtle
        this.connectParticles();

        this.animationId = requestAnimationFrame(this.animate);
    }

    connectParticles() {
        for (let a = 0; a < this.particles.length; a++) {
            for (let b = a; b < this.particles.length; b++) {
                let dx = this.particles[a].x - this.particles[b].x;
                let dy = this.particles[a].y - this.particles[b].y;
                let distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < this.connectionDistance) {
                    let opacity = 1 - (distance / this.connectionDistance);
                    this.ctx.strokeStyle = 'rgba(0, 188, 212, ' + opacity * 0.2 + ')'; // Cyan with low opacity
                    this.ctx.lineWidth = 1;
                    this.ctx.beginPath();
                    this.ctx.moveTo(this.particles[a].x, this.particles[a].y);
                    this.ctx.lineTo(this.particles[b].x, this.particles[b].y);
                    this.ctx.stroke();
                }
            }
        }
    }
}

// --- Global Initialization Logic ---

let currentSimulation = null;

function initProjector() {
    // Cleanup existing if any (prevent leaks on swap)
    if (currentSimulation) {
        currentSimulation.destroy();
        currentSimulation = null;
    }

    // Check if canvas exists in DOM
    if (document.getElementById('projector-canvas')) {
        currentSimulation = new InteractiveFloor();
        console.log("Interactive Floor Projector Initialized");
    }
}

// 1. Run on initial load
document.addEventListener('DOMContentLoaded', initProjector);

// 2. Run on HTMX Content Swap (if the new content contains the canvas)
document.body.addEventListener('htmx:afterSwap', (evt) => {
    // We can check evt.detail.target or just re-run init safely
    initProjector();
});

// 3. Cleanup on 'htmx:beforeSwap' if we are removing the section
document.body.addEventListener('htmx:beforeSwap', (evt) => {
    // If the target being swapped out contains our canvas, destroy it
    if (evt.detail.target.querySelector('#projector-canvas')) {
        if (currentSimulation) {
            currentSimulation.destroy();
            currentSimulation = null;
        }
    }
});
