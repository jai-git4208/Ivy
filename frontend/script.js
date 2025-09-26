
class GradientOrbApp {
    constructor() {
        this.orb = document.getElementById('gradientOrb');
        this.helloText = document.getElementById('helloText');
        this.copyrightSymbol = document.getElementById('copyrightSymbol');
        this.particlesContainer = document.getElementById('particles');
        
        this.isInteractive = true;
        this.particles = [];
        this.maxParticles = 20;
        
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.createParticles();
        this.startAnimationLoop();
        
        // Add initial delay for smoother load
        setTimeout(() => {
            document.body.style.opacity = '1';
        }, 100);
    }

    setupEventListeners() {
        // Orb interactions
        this.orb.addEventListener('mouseenter', () => this.onOrbHover());
        this.orb.addEventListener('mouseleave', () => this.onOrbLeave());
        this.orb.addEventListener('click', () => this.onOrbClick());
        
        // Copyright symbol interaction
        this.copyrightSymbol.addEventListener('click', (e) => {
            e.stopPropagation();
            this.onCopyrightClick();
        });
        
        // Keyboard interactions
        document.addEventListener('keydown', (e) => this.onKeyPress(e));
        
        // Window resize
        window.addEventListener('resize', () => this.onResize());
        
        // Mouse move for parallax effect
        document.addEventListener('mousemove', (e) => this.onMouseMove(e));
    }

    onOrbHover() {
        this.orb.style.filter = 'brightness(1.2) saturate(1.3)';
        this.createBurstParticles();
    }

    onOrbLeave() {
        this.orb.style.filter = '';
    }

    onOrbClick() {
        // Create ripple effect
        this.createRippleEffect();
        
        // Temporarily boost animation
        this.orb.style.animationDuration = '1s';
        setTimeout(() => {
            this.orb.style.animationDuration = '4s';
        }, 2000);
    }

    onCopyrightClick() {
        // Cycle through different text options
        const texts = ['Hello World!', 'Welcome!', 'Greetings!', 'Salutations!'];
        const currentText = this.helloText.childNodes[0].textContent.trim();
        const currentIndex = texts.indexOf(currentText);
        const nextIndex = (currentIndex + 1) % texts.length;
        
        this.helloText.childNodes[0].textContent = texts[nextIndex] + ' ';
        
        // Add bounce effect
        this.helloText.style.transform = 'scale(1.1)';
        setTimeout(() => {
            this.helloText.style.transform = '';
        }, 200);
    }

    onKeyPress(e) {
        switch(e.key) {
            case ' ':
                e.preventDefault();
                this.onOrbClick();
                break;
            case 'p':
                this.toggleParticles();
                break;
            case 'r':
                this.randomizeColors();
                break;
        }
    }

    onResize() {
        // Recreate particles for new screen size
        this.clearParticles();
        setTimeout(() => this.createParticles(), 100);
    }

    onMouseMove(e) {
        // Subtle parallax effect
        const x = (e.clientX / window.innerWidth - 0.5) * 20;
        const y = (e.clientY / window.innerHeight - 0.5) * 20;
        
        this.orb.style.transform = `translate(${x}px, ${y}px)`;
    }

    createParticles() {
        for (let i = 0; i < this.maxParticles; i++) {
            setTimeout(() => this.addParticle(), i * 200);
        }
    }

    addParticle() {
        const particle = document.createElement('div');
        particle.className = 'particle';
        
        // Random position
        particle.style.left = Math.random() * 100 + '%';
        
        // Random animation duration
        const duration = 3 + Math.random() * 4;
        particle.style.animationDuration = duration + 's';
        
        // Random delay
        particle.style.animationDelay = Math.random() * 2 + 's';
        
        // Random size
        const size = 2 + Math.random() * 4;
        particle.style.width = size + 'px';
        particle.style.height = size + 'px';
        
        this.particlesContainer.appendChild(particle);
        this.particles.push(particle);
        
        // Remove particle after animation
        setTimeout(() => {
            if (particle.parentNode) {
                particle.parentNode.removeChild(particle);
                const index = this.particles.indexOf(particle);
                if (index > -1) {
                    this.particles.splice(index, 1);
                }
            }
        }, duration * 1000 + 2000);
    }

    createBurstParticles() {
        for (let i = 0; i < 10; i++) {
            setTimeout(() => this.addParticle(), i * 50);
        }
    }

    createRippleEffect() {
        const ripple = document.createElement('div');
        ripple.style.cssText = `
            position: absolute;
            border: 2px solid rgba(255, 255, 255, 0.5);
            border-radius: 50%;
            width: 0;
            height: 0;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
            pointer-events: none;
            animation: ripple 0.8s ease-out;
        `;
        
        // Add ripple keyframes if not exists
        if (!document.getElementById('ripple-style')) {
            const style = document.createElement('style');
            style.id = 'ripple-style';
            style.textContent = `
                @keyframes ripple {
                    to {
                        width: 500px;
                        height: 500px;
                        opacity: 0;
                    }
                }
            `;
            document.head.appendChild(style);
        }
        
        this.orb.appendChild(ripple);
        
        setTimeout(() => {
            if (ripple.parentNode) {
                ripple.parentNode.removeChild(ripple);
            }
        }, 800);
    }

    toggleParticles() {
        this.particlesContainer.style.display = 
            this.particlesContainer.style.display === 'none' ? 'block' : 'none';
    }

    randomizeColors() {
        const colors = [
            'linear-gradient(135deg, #ff6b9d, #c794f6, #7c3aed)',
            'linear-gradient(135deg, #06b6d4, #3b82f6, #8b5cf6)',
            'linear-gradient(135deg, #f59e0b, #ef4444, #ec4899)',
            'linear-gradient(135deg, #10b981, #06b6d4, #8b5cf6)'
        ];
        
        const randomColor = colors[Math.floor(Math.random() * colors.length)];
        const layer1 = document.querySelector('.layer-1');
        layer1.style.background = randomColor;
    }

    clearParticles() {
        this.particles.forEach(particle => {
            if (particle.parentNode) {
                particle.parentNode.removeChild(particle);
            }
        });
        this.particles = [];
    }

    startAnimationLoop() {
        // Continuous particle generation
        setInterval(() => {
            if (this.particles.length < this.maxParticles) {
                this.addParticle();
            }
        }, 1000);
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new GradientOrbApp();
});

// Smooth loading
document.body.style.opacity = '0';
document.body.style.transition = 'opacity 0.5s ease';
