// DivergenceAI Landing Page Application
// Handles animations, modals, forms, and user interactions

/**
 * ANIMATION SYSTEM
 */
class AnimationManager {
    constructor() {
        this.animations = new Map();
        this.animationId = null;
        this.isPaused = false;
    }

    setupCanvas(canvas) {
        const dpr = window.devicePixelRatio || 1;
        canvas.width = canvas.offsetWidth * dpr;
        canvas.height = canvas.offsetHeight * dpr;
        const ctx = canvas.getContext('2d');
        ctx.scale(dpr, dpr);
        return { width: canvas.offsetWidth, height: canvas.offsetHeight };
    }

    initNeuralNetwork() {
        const canvas = document.getElementById('neuralNetworkCanvas');
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        const { width, height } = this.setupCanvas(canvas);
        
        // Adjust particle count based on screen size for better mobile performance
        const isMobile = window.innerWidth <= 768;
        const particleCount = isMobile ? 12 : 20;
        const neurons = this.generateNeurons(width, height, particleCount);

        let lastTime = 0;
        const targetFPS = isMobile ? 30 : 60; // Lower FPS on mobile for better performance
        const frameInterval = 1000 / targetFPS;

        const animate = (currentTime) => {
            if (!this.isPaused) {
                if (currentTime - lastTime >= frameInterval) {
                    this.drawNeuralNetwork(ctx, width, height, neurons, isMobile);
                    lastTime = currentTime;
                }
            }
            this.animationId = requestAnimationFrame(animate);
        };

        animate(0);
    }

    generateNeurons(width, height, count) {
        const neurons = [];
        for (let i = 0; i < count; i++) {
            neurons.push({
                x: Math.random() * width,
                y: Math.random() * height,
                radius: Math.random() * 2 + 1,
                vx: (Math.random() - 0.5) * 0.5,
                vy: (Math.random() - 0.5) * 0.5
            });
        }
        return neurons;
    }

    drawNeuralNetwork(ctx, width, height, neurons, isMobile = false) {
        ctx.clearRect(0, 0, width, height);

        // Update neuron positions
        neurons.forEach(neuron => {
            neuron.x += neuron.vx;
            neuron.y += neuron.vy;

            // Bounce off walls
            if (neuron.x < 0 || neuron.x > width) neuron.vx *= -1;
            if (neuron.y < 0 || neuron.y > height) neuron.vy *= -1;
        });

        // Draw connections with reduced distance on mobile for better performance
        const maxDistance = isMobile ? 80 : 100;
        for (let i = 0; i < neurons.length; i++) {
            for (let j = i + 1; j < neurons.length; j++) {
                const dx = neurons[i].x - neurons[j].x;
                const dy = neurons[i].y - neurons[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < maxDistance) {
                    ctx.beginPath();
                    ctx.moveTo(neurons[i].x, neurons[i].y);
                    ctx.lineTo(neurons[j].x, neurons[j].y);
                    const opacity = (maxDistance - distance) / maxDistance;
                    const alpha = isMobile ? opacity * 0.15 : opacity * 0.2; // Slightly more transparent on mobile
                    ctx.strokeStyle = `rgba(0, 229, 255, ${alpha})`;
                    ctx.stroke();
                }
            }
        }

        // Draw neurons
        neurons.forEach(neuron => {
            ctx.beginPath();
            ctx.arc(neuron.x, neuron.y, neuron.radius, 0, Math.PI * 2);
            ctx.fillStyle = '#00E5FF';
            ctx.fill();
        });
    }

    pauseAnimations() {
        this.isPaused = true;
    }

    resumeAnimations() {
        this.isPaused = false;
    }
}

/**
 * MODAL SYSTEM
 */
class ModalManager {
    static show(modalId, overlayId) {
        const modal = document.getElementById(modalId);
        const overlay = document.getElementById(overlayId);
        if (modal) modal.style.display = "block";
        if (overlay) overlay.style.display = "block";
    }

    static hide(modalId, overlayId) {
        const modal = document.getElementById(modalId);
        const overlay = document.getElementById(overlayId);
        if (modal) modal.style.display = "none";
        if (overlay) overlay.style.display = "none";
    }
}

/**
 * ANALYTICS SYSTEM
 */
class Analytics {
    static captureEvent(eventName, properties = {}) {
        fetch('/capture-event', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                event: eventName,
                ...properties
            })
        }).catch(error => console.error('Analytics error:', error));
    }
}

/**
 * FORM HANDLER
 */
class FormHandler {
    static async submitContactForm() {
        const company = document.getElementById("company").value;
        const contactEmail = document.getElementById("contactEmail").value;
        const teamSize = document.getElementById("teamSize").value;
        const requirements = document.getElementById("requirements").value;
        const resultDiv = document.getElementById('contactFormResult');
        
        if (!company || !contactEmail || !teamSize || !requirements) {
            alert("Please fill out all fields.");
            return;
        }

        resultDiv.innerHTML = "Please wait...";
        
        const data = {
            access_key: 'af5f23cb-d08f-4578-b508-8ae2e3edd453',
            company,
            email: contactEmail,
            team_size: teamSize,
            requirements,
            form_type: 'enterprise_contact'
        };

        try {
            const response = await fetch('https://api.web3forms.com/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            
            if (response.status === 200) {
                resultDiv.innerHTML = "Thank you! We'll get back to you within 24 hours.";
                resultDiv.style.color = "#38bdf8";
                
                // Clear form and close modal after delay
                setTimeout(() => {
                    FormHandler.clearContactForm();
                    closeContactModal();
                    resultDiv.innerHTML = "";
                }, 3000);

                // Track conversion
                Analytics.captureEvent('enterprise_contact_form_submitted', {
                    email: contactEmail,
                    company,
                    team_size: teamSize
                });
            } else {
                resultDiv.innerHTML = result.message;
                resultDiv.style.color = "#ef4444";
            }
        } catch (error) {
            console.error('Form submission error:', error);
            resultDiv.innerHTML = "Something went wrong! Please try again.";
            resultDiv.style.color = "#ef4444";
        }
    }

    static clearContactForm() {
        const fields = ['company', 'contactEmail', 'teamSize', 'requirements'];
        fields.forEach(id => {
            const element = document.getElementById(id);
            if (element) element.value = "";
        });
    }
}

/**
 * NAVIGATION UTILITIES
 */
class Navigation {
    static enableSmoothScrolling() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }
}

/**
 * GLOBAL FUNCTIONS (for HTML onclick handlers)
 */
function showContactModal() {
    ModalManager.show('contactModal', 'contactOverlay');
}

function closeContactModal() {
    ModalManager.hide('contactModal', 'contactOverlay');
}

function showDemoModal() {
    ModalManager.show('demoModal', 'demoOverlay');
    Analytics.captureEvent('demo_video_opened');
}

function closeDemoModal() {
    ModalManager.hide('demoModal', 'demoOverlay');
}

function submitContactForm() {
    FormHandler.submitContactForm();
}

function simpleEventCapture(eventName) {
    Analytics.captureEvent(eventName);
}

function showImageModal(imageSrc, imageAlt) {
    const expandedImage = document.getElementById('expandedImage');
    const imageCaption = document.getElementById('imageCaption');
    
    if (expandedImage && imageCaption) {
        expandedImage.src = imageSrc;
        expandedImage.alt = imageAlt;
        imageCaption.textContent = imageAlt;
        
        ModalManager.show('imageModal', 'imageOverlay');
        Analytics.captureEvent('demo_image_expanded', { image: imageSrc });
    }
}

function closeImageModal() {
    ModalManager.hide('imageModal', 'imageOverlay');
}

function toggleMobileMenu() {
    const hamburger = document.querySelector('.hamburger-menu');
    const navMenu = document.getElementById('navMenu');
    
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
}

function closeMobileMenu() {
    const hamburger = document.querySelector('.hamburger-menu');
    const navMenu = document.getElementById('navMenu');
    
    hamburger.classList.remove('active');
    navMenu.classList.remove('active');
}

/**
 * APPLICATION INITIALIZATION
 */
class App {
    constructor() {
        this.animationManager = new AnimationManager();
        this.init();
    }

    init() {
        // Wait for DOM to be ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.startup());
        } else {
            this.startup();
        }
    }

    startup() {
        // Initialize animations
        this.animationManager.initNeuralNetwork();
        
        // Enable smooth scrolling for anchor links
        Navigation.enableSmoothScrolling();
        
        // Handle mobile menu link clicks
        document.querySelectorAll('.nav-menu a').forEach(link => {
            link.addEventListener('click', () => {
                closeMobileMenu();
            });
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', (event) => {
            const hamburger = document.querySelector('.hamburger-menu');
            const navMenu = document.getElementById('navMenu');
            
            if (!hamburger.contains(event.target) && !navMenu.contains(event.target)) {
                closeMobileMenu();
            }
        });
        
        // Handle window resize for responsive canvas
        window.addEventListener('resize', () => {
            this.animationManager.initNeuralNetwork();
        });

        // Pause animations when page is not visible (saves battery on mobile)
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                this.animationManager.pauseAnimations();
            } else {
                this.animationManager.resumeAnimations();
            }
        });

        // Handle Esc key for closing modals and mobile menu
        document.addEventListener('keydown', (event) => {
            if (event.key === 'Escape') {
                // Close mobile menu if open
                closeMobileMenu();
                
                // Close demo modal if open
                const demoModal = document.getElementById('demoModal');
                if (demoModal && demoModal.style.display === 'block') {
                    closeDemoModal();
                }
                
                // Close contact modal if open
                const contactModal = document.getElementById('contactModal');
                if (contactModal && contactModal.style.display === 'block') {
                    closeContactModal();
                }
                
                // Close image modal if open
                const imageModal = document.getElementById('imageModal');
                if (imageModal && imageModal.style.display === 'block') {
                    closeImageModal();
                }
            }
        });

        console.log('DivergenceAI app initialized');
    }
}

// Start the application
new App();