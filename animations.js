// EM Wave Animation
const emWaveCanvas = document.getElementById('emWaveCanvas');
const emWaveCtx = emWaveCanvas.getContext('2d');

function setupCanvas(canvas) {
    const dpr = window.devicePixelRatio || 1;
    canvas.width = canvas.offsetWidth * dpr;
    canvas.height = canvas.offsetHeight * dpr;
    const ctx = canvas.getContext('2d');
    ctx.scale(dpr, dpr);
    return { width: canvas.offsetWidth, height: canvas.offsetHeight };
}

function animateEMWave() {
    const { width, height } = setupCanvas(emWaveCanvas);
    let time = 0;

    function drawWave() {
        emWaveCtx.clearRect(0, 0, width, height);
        
        // Create gradient
        const gradient = emWaveCtx.createLinearGradient(0, 0, width, 0);
        gradient.addColorStop(0, 'rgba(0, 229, 255, 0.5)');
        gradient.addColorStop(1, 'rgba(0, 102, 255, 0.5)');

        const waveLength = 0.018;
        const amplitude = 1;
        const frequency = 0.1;

        for (let x = 0; x < width; x += 10) {
            for (let y = 0; y < height; y += 10) {
                const distanceFromCenter = Math.sqrt((x - width / 2) ** 2 + (y - height / 2) ** 2);
                const z = amplitude * Math.sin(waveLength * distanceFromCenter - frequency * time);
                
                const size = Math.max(0, (z + amplitude) / (2 * amplitude));
                const alpha = size * 0.3;
                emWaveCtx.beginPath();
                emWaveCtx.arc(x, y, size * 5, 0, Math.PI * 2);
                emWaveCtx.fillStyle = `rgba(0, 229, 255, ${alpha})`;
                emWaveCtx.fill();
            }
        }

        time += 0.5;
        requestAnimationFrame(drawWave);
    }

    drawWave();

    // Resize canvas when window is resized
    window.addEventListener('resize', () => {
        const { width, height } = setupCanvas(emWaveCanvas);
    });
}

// Neural Network Animation
const nnCanvas = document.getElementById('neuralNetworkCanvas');
const nnCtx = nnCanvas.getContext('2d');

function animateNeuralNetwork() {
    const { width, height } = setupCanvas(nnCanvas);
    const neurons = [];
    const numNeurons = 20;

    for (let i = 0; i < numNeurons; i++) {
        neurons.push({
            x: Math.random() * width,
            y: Math.random() * height,
            radius: Math.random() * 2 + 1,
            vx: (Math.random() - 0.5) * 0.5,
            vy: (Math.random() - 0.5) * 0.5
        });
    }

    function drawNeurons() {
        nnCtx.clearRect(0, 0, width, height);

        // Update positions
        neurons.forEach(neuron => {
            neuron.x += neuron.vx;
            neuron.y += neuron.vy;

            // Bounce off walls
            if (neuron.x < 0 || neuron.x > width) neuron.vx *= -1;
            if (neuron.y < 0 || neuron.y > height) neuron.vy *= -1;
        });

        // Draw connections
        for (let i = 0; i < neurons.length; i++) {
            for (let j = i + 1; j < neurons.length; j++) {
                const dx = neurons[i].x - neurons[j].x;
                const dy = neurons[i].y - neurons[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);

                if (distance < 100) {
                    nnCtx.beginPath();
                    nnCtx.moveTo(neurons[i].x, neurons[i].y);
                    nnCtx.lineTo(neurons[j].x, neurons[j].y);
                    const opacity = (100 - distance) / 100;
                    nnCtx.strokeStyle = `rgba(0, 229, 255, ${opacity * 0.2})`;
                    nnCtx.stroke();
                }
            }
        }

        // Draw neurons
        neurons.forEach(neuron => {
            nnCtx.beginPath();
            nnCtx.arc(neuron.x, neuron.y, neuron.radius, 0, Math.PI * 2);
            nnCtx.fillStyle = '#00E5FF';
            nnCtx.fill();
        });

        requestAnimationFrame(drawNeurons);
    }

    drawNeurons();
}

function showModal() {
    document.getElementById("modal").style.display = "block";
    document.getElementById("overlay").style.display = "block";
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
    document.getElementById("overlay").style.display = "none";
}

function submitForm() {
    let access_key = document.getElementById("access_key").value;
    let email = document.getElementById("email").value;
    let request = document.getElementById("request").value;
    const resultDiv = document.getElementById('heroFormResult'); // Find the result div for this form
    const ctaResultDiv = document.getElementById('ctaFormResult'); // Find the result div for this form
    
    resultDiv.innerHTML = "Please wait..."
    ctaResultDiv.innerHTML = "Please wait..."
    if (email && request) {
        
        data = {
            access_key: access_key,
            email: email,
            request: request
        }
        // console.log(json);
        json = JSON.stringify(data)

        fetch('https://api.web3forms.com/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: json
            })
            .then(async (response) => {
                let json = await response.json();
                if (response.status == 200) {
                    resultDiv.innerHTML = "Form submitted successfully";
                    ctaResultDiv.innerHTML = "Form submitted successfully";
                } else {
                    console.log(response);
                    resultDiv.innerHTML = json.message;
                    ctaResultDiv.innerHTML = json.message;
                }
            })
            .catch(error => {
                console.log(error);
                resultDiv.innerHTML = "Something went wrong!";
                ctaResultDiv.innerHTML = "Something went wrong!";
            })
            .then(function() {
                form.reset();
                setTimeout(() => {
                    resultDiv.style.display = "none";
                    ctaResultDiv.style.display = "none";
                }, 3000);
            });
    
        // Send PostHog event
        fetch('/capture-event', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: email,
                request: request,
                event: 'waitlist_form_submitted'
            })
        });
        console.log("PostHog event sent");
        closeModal();
    } else {
        alert("Please fill out all fields.");
    }
}




// Start animations when the page loads
window.addEventListener('load', () => {
    // animateEMWave();
    animateNeuralNetwork();
    
    // Trigger a resize event to ensure canvas is properly sized
    window.dispatchEvent(new Event('resize'));
});




// Form submission
const form = document.getElementById('heroForm');
const forms = document.querySelectorAll('#heroForm', '#ctaForm', '#modal');
// const result = document.getElementById('result');

forms.forEach(form => {
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(form);
  const object = Object.fromEntries(formData);
  console.log(object);
  const json = JSON.stringify(object);
  const resultDiv = form.querySelector('.result'); // Find the result div for this form
  resultDiv.innerHTML = "Please wait..."

    fetch('https://api.web3forms.com/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: json
        })
        .then(async (response) => {
            let json = await response.json();
            if (response.status == 200) {
                resultDiv.innerHTML = "Form submitted successfully";
            } else {
                console.log(response);
                resultDiv.innerHTML = json.message;
            }
        })
        .catch(error => {
            console.log(error);
            resultDiv.innerHTML = "Something went wrong!";
        })
        .then(function() {
            form.reset();
            setTimeout(() => {
                resultDiv.style.display = "none";
            }, 3000);
        });
    });
});

// Contact Modal Functions
function showContactModal() {
    document.getElementById("contactModal").style.display = "block";
    document.getElementById("contactOverlay").style.display = "block";
}

function closeContactModal() {
    document.getElementById("contactModal").style.display = "none";
    document.getElementById("contactOverlay").style.display = "none";
}

function submitContactForm() {
    let company = document.getElementById("company").value;
    let contactEmail = document.getElementById("contactEmail").value;
    let teamSize = document.getElementById("teamSize").value;
    let requirements = document.getElementById("requirements").value;
    const resultDiv = document.getElementById('contactFormResult');
    
    resultDiv.innerHTML = "Please wait..."
    
    if (company && contactEmail && teamSize && requirements) {
        
        data = {
            access_key: 'af5f23cb-d08f-4578-b508-8ae2e3edd453', // Using the same access key
            company: company,
            email: contactEmail,
            team_size: teamSize,
            requirements: requirements,
            form_type: 'enterprise_contact'
        }
        
        json = JSON.stringify(data)

        fetch('https://api.web3forms.com/submit', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: json
            })
            .then(async (response) => {
                let json = await response.json();
                if (response.status == 200) {
                    resultDiv.innerHTML = "Thank you! We'll get back to you within 24 hours.";
                    resultDiv.style.color = "#38bdf8";
                } else {
                    console.log(response);
                    resultDiv.innerHTML = json.message;
                    resultDiv.style.color = "#ef4444";
                }
            })
            .catch(error => {
                console.log(error);
                resultDiv.innerHTML = "Something went wrong! Please try again.";
                resultDiv.style.color = "#ef4444";
            })
            .then(function() {
                setTimeout(() => {
                    // Clear form and close modal after successful submission
                    if (resultDiv.innerHTML.includes("Thank you")) {
                        document.getElementById("company").value = "";
                        document.getElementById("contactEmail").value = "";
                        document.getElementById("teamSize").value = "";
                        document.getElementById("requirements").value = "";
                        closeContactModal();
                    }
                    resultDiv.innerHTML = "";
                }, 3000);
            });
    
        // Send PostHog event
        fetch('/capture-event', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: contactEmail,
                company: company,
                team_size: teamSize,
                event: 'enterprise_contact_form_submitted'
            })
        });
        console.log("PostHog event sent for enterprise contact");
        closeContactModal();
    } else {
        alert("Please fill out all fields.");
    }
}



