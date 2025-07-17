from fasthtml.common import *
from posthog import Posthog
import uuid

posthog = Posthog(project_api_key='phc_864zsK9T6F93dirU0dvYqnArsDAwqi4OhgFAppnKNex', host='https://us.i.posthog.com')


app, rt = fast_app(
    hdrs=(
        Title('divergenceAI | Research for Teams'),
        # Style(styling_string),
        Link(rel="stylesheet", href="styles.css"),
    ),
    live=True)


head = Head(
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Title('DivergenceAI - Advanced Electromagnetic Simulation Tool'),
        Link(rel='stylesheet', href='styles.css'),
        Script(src='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js'),
    )

header = Header(
                Div(
                A(
                    Svg(
                        Path(d='m21.64 3.64-1.28-1.28a1.21 1.21 0 0 0-1.72 0L2.36 18.64a1.21 1.21 0 0 0 0 1.72l1.28 1.28a1.2 1.2 0 0 0 1.72 0L21.64 5.36a1.2 1.2 0 0 0 0-1.72Z'),
                        Path(d='m14 7 3 3'),
                        Path(d='M5 6v4'),
                        Path(d='M19 14v4'),
                        Path(d='M10 2v2'),
                        Path(d='M7 8H3'),
                        Path(d='M21 16h-4'),
                        Path(d='M11 3H9'),
                        xmlns='http://www.w3.org/2000/svg',
                        width='24',
                        height='24',
                        viewbox='0 0 24 24',
                        fill='none',
                        stroke='currentColor',
                        stroke_width='2',
                        stroke_linecap='round',
                        stroke_linejoin='round',
                        cls='lucide lucide-wand-2'
                    ),
                    
                    H1(Span('\\( \\nabla \\cdot \\) AI'), style='display: inline-block; margin-right: 2rem;'),
                    H2(Span('DivergenceAI'), style='display: inline-block; margin-right: 1rem;'),
                    href='/',
                    cls='logo'
                ),
                Nav(
                    # A('Features', href='#features'),
                    A('Benefits', href='#benefits'),
                    A('Pricing', href='#pricing'),
                    A('Blog', href='/blog', cls='active'),
                    A(Button('Join the beta', cls='btn btn-primary'), href='#pricing')
                ),
                cls='container'
            )
        )

footer = Footer(
            Div(
                P('© 2025 DivergenceAI. All rights reserved.', cls='copyright-text'),
                A(
                    Span('🗨️ Talk to us: Calendar link', cls='contact-text'), # The text next to the icon
                    href='https://calendar.app.google/GFN7FhktzVMAc1Th7',
                    cls='footer-contact-link'
                ),
                cls='container footer-content' # Added 'footer-content' for flexbox styling
            )
)

@app.get("/")
def home(session):
    """Checks if user has an ID, creates one if not, and returns it"""
    user_id = session.get('user_id')
    if not user_id:
        user_id = str(uuid.uuid4())
        session['user_id'] = user_id    
    
    # Track homepage view server-side
    posthog.capture('home_page_viewed', distinct_id=user_id)

    # --- YouTube Video Setup ---
    youtube_video_id = "6Jn3-z7b1Xw"#"TJTgeH5fO7o" # Replace with your actual video ID, e.g., 'dQw4w9WgXcQ'
    # Common parameters for a seamless hero video:
    # autoplay=1: Start playing automatically (requires mute=1 in most browsers)
    # mute=1: Start muted
    # loop=1&playlist=VIDEO_ID: Loop the video (playlist trick for single videos)
    # controls=0: Hide player controls
    # modestbranding=1: Reduce YouTube logo (optional)
    # showinfo=0: Hide video title and uploader (deprecated, but sometimes works)
    # autohide=1: Autohide controls (if controls were visible)
    youtube_embed_url = f"https://www.youtube.com/embed/{youtube_video_id}?autoplay=1&mute=1&loop=1&playlist={youtube_video_id}&controls=0&modestbranding=1&showinfo=0&autohide=1&start=33&end=166"

    video_iframe = Iframe(
        src=youtube_embed_url,
        title="DivergenceAI Product Showcase", # Descriptive title for accessibility
        frameborder="0",
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share",
        allowfullscreen=True, # Note: fasthtml handles boolean attributes correctly
        cls="hero-youtube-iframe" # Add a class for easier CSS targeting
    )
    # --- End YouTube Video Setup ---


    return Html(
        head,
        Body(
            header,
            Main(
                Section(
                    Canvas(id='emWaveCanvas'), # This is your existing canvas
                    Div( # This is the existing Div(cls='container')
                        # We'll make this container a flex parent for side-by-side layout
                        Div( # This is the existing Div(cls='hero-content')
                            H1(Span('AI-powered Engineering Simulations'), cls='hero-h1'),
                            P('From CAD to insights in seconds. Streamline your workflow with AI—faster design cycles, smarter decisions, and seamless engineering.'),
                            # Button('Join the beta', onclick='showModal()', cls='waitlist-btn'),
                            A(Button('Join the beta', cls='btn btn-primary'), href='#pricing'),
                            Div(id='overlay', onclick='closeModal()', cls='overlay'),
                            Div(
                                Button('X', onclick='closeModal()', cls='close-btn'),
                                H3('Join the beta'),
                                Label('Email:', fr='email'), # 'for' attribute is 'fr' in fasthtml
                                Input(type='hidden', name='access_key', id='access_key', value='af5f23cb-d08f-4578-b508-8ae2e3edd453'),
                                Input(type='email', id='email', required='', placeholder='Enter your email'),
                                Label('What would you like Divergence AI to do for you?', fr='request'),
                                Textarea(id='request', rows='4', required='', placeholder="Imagine this is DivergenceAI's input box, what would you ask it to do?"),
                                Button('Submit', onclick='submitForm()', cls='btn btn-contact'),
                                id='modal',
                                cls='modal'
                            ),
                            Div(cls='result', id='heroFormResult'),
                            cls='hero-content' # This div will be one flex item (text content)
                        ),
                        # --- New Div to wrap the video iframe ---
                        Div(
                            video_iframe,
                            cls='hero-video-wrapper' # This div will be the other flex item (video)
                        ),
                        # --- End New Div ---
                        cls='container hero-layout-container' # Added 'hero-layout-container' for flex styling
                    ),
                cls='hero'
            ),
            Section(
                H1('The Current Simulation Landscape'),
                Div(
                    Div(
                        H2('Slow set up time'),
                        P('The flow from idea to simulation takes weeks if not months.'),
                        cls='card'
                    ),
                    Div(
                        H2('Complex'),
                        P('Requires deep technical expertise, limiting accessibility for many users.'),
                        cls='card'
                    ),
                    Div(
                        H2('Time-consuming'),
                        P('Slow iteration process hampers rapid prototyping and innovation.'),
                        cls='card'
                    ),
                    Div(
                        H2('Expensive'),
                        P('Inaccessible to non-established companies. Open source tools are even more complex.'),
                        cls='card'
                    ),
                    cls='grid'
                ),
                cls='simulation-landscape'
            ),
            Section(
                Canvas(id='neuralNetworkCanvas'),
                Div(
                    Div(
                        H1('Traditional Simulation Workflow', cls='workflows-title-muted'),
                        Div(
                            Div('1', cls='step-number'),
                            Div(
                                    H2('Model intake and preparation'),
                                    P('Import 3D CAD file, simplify geometry and create mesh for discretization.'),
                                    cls='step-content'
                                ),
                                cls='step'
                            ),
                            Div(
                                Div('2', cls='step-number'),
                                Div(
                                    H2('Simulation Setup'),
                                    P('Define constraints, material properties, boundary conditions and solver parameters.'),
                                    cls='step-content'
                                ),
                                cls='step'
                            ),
                            Div(
                                Div('3', cls='step-number'),
                                Div(
                                    H2('Computation'),
                                    P('Run simulations, taking hours or days depending on complexity.'),
                                    cls='step-content'
                                ),
                                cls='step'
                            ),
                            Div(
                                Div('4', cls='step-number'),
                                Div(
                                    H2('Analysis'),
                                    P('Extract insights like field distributions or impedance values.'),
                                    cls='step-content'
                                ),
                                cls='step'
                            ),
                            Div(
                                Div('5', cls='step-number'),
                                Div(
                                    H2('Scenario Exploration'),
                                    P('Vary conditions to evaluate performance across design spaces.'),
                                    cls='step-content'
                                ),
                                cls='step'
                            ),
                            cls='workflow-column'
                        ),
                        Div(
                            H1('AI improved Workflow', cls='workflows-title'),
                            Div(
                                Div('1', cls='step-number'),
                                Div(
                                    H2('Automatic Preprocessing and Smart Meshing'),
                                    P('Onboard geometry, simplify, iterate meshing, set up boundary conditions and simulation parameters.'),
                                    cls='step-content'
                                ),
                                cls='step'
                            ),
                            Div(
                                Div('2', cls='step-number'),
                                Div(
                                    H2('Run Simulations with Autonomous Monitoring'),
                                    P('Simulations often fail. Our monitoring agent detects issues in real-time, attempts to debug, and re-runs automatically to minimize downtime.'),
                                    cls='step-content'
                                ),
                                cls='step'
                            ),
                            Div(
                                Div('3', cls='step-number'),
                                Div(
                                    H2('AI-Powered Postprocessing & Insights'),
                                    P('Intuitive natural language interface allows users to interact with simulation results. The AI generates key visualizations, highlights insights, and enables easy sharing - making high-fidelity simulations more accessible to engineers.'),
                                    cls='step-content'
                                ),
                                    cls='step'
                            ),
                        cls='workflow-column'
                        ),
                    cls='workflow-container'
                    ),
                cls='workflows'
            ),
            Section(
                Div(
                    H2('Key Benefits', cls='benefits-title'),
                    Div(
                        Div(
                            H3('AI-Powered Postprocessing & Insights'),
                            P('Intuitive natural language interface allows users to interact with simulation results. The AI generates key visualizations, highlights insights, and enables easy sharing - making high-fidelity simulations more accessible to engineers.'),
                            cls='benefit-card'
                        ),
                        Div(
                            H3('Run Simulations with Autonomous Monitoring'),
                            P('Simulations often fail. Our monitoring agent detects issues in real-time, attempts to debug, and re-runs automatically to minimize downtime.'),
                            cls='benefit-card'
                        ),
                        Div(
                            H3('Automatic Preprocessing and Smart Meshing'),
                            P('Onboard geometry, simplify, iterate meshing, set up boundary conditions and simulation parameters.'),
                            cls='benefit-card'
                        ),
                        cls='benefits-grid'
                    ),
                    cls='container'
                ),
                id='benefits'
            ),
            Section(
                Div(
                    H2('Pricing Plans', cls='pricing-title'),
                    P('Choose the plan that fits your stage—help shape the future or scale with confidence.', cls='pricing-subtitle'),
                    Div(
                        Div(
                            H3('Community Tier', cls='tier-title'),
                            Div('$0', cls='tier-price'),
                            P('per month', cls='tier-period'),
                            Ul(
                                Li('Full access to core simulation assistant tools'),
                                Li('Community support (Slack)'),
                                Li('Design metadata may be used to improve models'),
                                cls='tier-features'
                            ),
                            P(
                                'This plan is free during the beta period. In exchange, we collect anonymized metadata and usage to help us improve the platform. Ideal for individuals, students, and early adopters shaping the future of simulation tools.',
                                cls='tier-description'
                            ),
                            P('🚀 Early access badge: Help us build faster with your feedback.', cls='tier-badge'),
                            A(Button('Get Started Free', cls='tier-btn tier-btn-free'), href='https://dashboard.app.divergenceai.xyz'),
                            cls='pricing-tier'
                        ),
                        Div(
                            H3('Enterprise Tier', cls='tier-title'),
                            Div('Contact Sales', cls='tier-price-contact'),
                            P('custom pricing', cls='tier-period'),
                            Ul(
                                Li('All core features'),
                                Li('Enhanced data isolation & encryption'),
                                Li('Usage controls & private deployments'),
                                Li('Priority support & feature requests'),
                                Li('No data used for model training'),
                                cls='tier-features'
                            ),
                            P(
                                'Built for companies with strict security and privacy needs. Includes full control over data, private deployments, and white-glove onboarding. Your data stays private—always.',
                                cls='tier-description'
                            ),
                            P('🛡️ We’re early—Enterprise pricing is flexible and based on your scale.', cls='tier-badge'),
                            Button('Contact Sales', onclick='showContactModal()', cls='tier-btn tier-btn-enterprise'),
                            cls='pricing-tier enterprise-tier'
                        ),
                        cls='pricing-grid'
                    ),
                    cls='container'
                ),

                # Contact Sales Modal
                Div(id='contactOverlay', onclick='closeContactModal()', cls='overlay'),
                Div(
                    Button('X', onclick='closeContactModal()', cls='close-btn'),
                    H3('Contact Sales'),
                    P('Tell us about your enterprise needs and we\'ll get back to you within 24 hours.'),
                    Label('Company Name:', fr='company'),
                    Input(type='text', id='company', required='', placeholder='Enter your company name'),
                    Label('Email:', fr='contactEmail'),
                    Input(type='email', id='contactEmail', required='', placeholder='Enter your email'),
                    Label('Team Size:', fr='teamSize'),
                    Select(
                        Option('1-10 employees', value='1-10'),
                        Option('11-50 employees', value='11-50'),
                        Option('51-200 employees', value='51-200'),
                        Option('200+ employees', value='200+'),
                        id='teamSize',
                        required=''
                    ),
                    Label('Tell us about your requirements:', fr='requirements'),
                    Textarea(id='requirements', rows='4', required='', placeholder='What are your specific security, privacy, or compliance needs?'),
                    Button('Submit', onclick='submitContactForm()', cls='btn btn-contact'),
                    id='contactModal',
                    cls='modal'
                ),
                Div(cls='result', id='contactFormResult'),
                id='pricing'
            ),
        #     Section(
        #         Div(
        #             H2('Ready to Transform Your Design Process?'),
        #             P('Join the waitlist and be the first to see how DivergenceAI can revolutionize your simulations.'),
                    
        #             # Wait list modal
        #             Button('Join the Waitlist', onclick='showModal()', cls='waitlist-btn'),
        #             Div(id='overlay', onclick='closeModal()', cls='overlay'),
        #             Div(
        #                 Button('X', onclick='closeModal()', cls='close-btn'),
        #                 H3('Join the Waitlist'),
        #                 Label('Email:', fr='email'),
        #                 Input(type='hidden', name='access_key', id='access_key', value='af5f23cb-d08f-4578-b508-8ae2e3edd453'),
        #                 Input(type='email', id='email', required='', placeholder='Enter your email'),
        #                 Label('What would you like Divergence AI to do for you?', fr='request'),
        #                 Textarea(id='request', rows='4', required='', placeholder="Imagine this is DivergenceAI's input box, what would you ask it to do?"),
        #                 Button('Submit', onclick='submitForm()', cls='btn btn-contact'),
        #                 id='modal',
        #                 cls='modal'
        #             ),
        #             Div(cls='result', id='ctaFormResult'),

        #             cls='container',
                    
        #         ),
        #         cls='cta',
        #         # id='cta'
        #     )
        # ),
        Section(
            Div(
                H2('Ready to Transform Your Design Process?'),
                P('Use the public beta of DivergenceAI today, and help shape the future of simulation.'),
                
                # Primary CTA: Try Beta Now
                A(Button('Try the Beta Now', cls='btn btn-contact'), href='https://dashboard.app.divergenceai.xyz'),  # Replace with actual beta link

                # Spacer between sections
                Div(cls='cta-spacer'),
                
                # Optional Feedback CTA
                P('Want to tell us what you’d like DivergenceAI to do for you?'),
                Button('Give Feedback', onclick='showModal()', cls='waitlist-btn'),  # Reuse modal for feedback input

                # Feedback Modal (formerly waitlist)
                Div(id='overlay', onclick='closeModal()', cls='overlay'),
                Div(
                    Button('X', onclick='closeModal()', cls='close-btn'),
                    H3('What should DivergenceAI do for you?'),
                    Label('Email:', fr='email'),
                    Input(type='hidden', name='access_key', id='access_key', value='af5f23cb-d08f-4578-b508-8ae2e3edd453'),
                    Input(type='email', id='email', required='', placeholder='Enter your email'),
                    Label('Imagine this is DivergenceAI’s input box. What would you ask it to do?', fr='request'),
                    Textarea(id='request', rows='4', required='', placeholder="What would you want DivergenceAI to simulate or analyze for you?"),
                    Button('Submit', onclick='submitForm()', cls='btn btn-contact'),
                    id='modal',
                    cls='modal'
                ),
                Div(cls='result', id='ctaFormResult'),

                cls='container',
            ),
            cls='cta',
            id='cta')
        ),
        footer,
        Script(src='animations.js')
    ),
    lang='en'
)

@app.get("/blog")
def blog(session):
    Style('.simulation-landscape {\r\n        font-family: Arial, sans-serif;\r\n        background-color: #0d0d0d;\r\n        color: white;\r\n        padding: 20px;\r\n        border-radius: 8px;\r\n    }\r\n    .simulation-landscape h1 {\r\n        font-size: 3em;\r\n        background: linear-gradient(90deg, #c084fc, #60a5fa);\r\n        -webkit-background-clip: text;\r\n        -webkit-text-fill-color: transparent;\r\n    }\r\n    .grid {\r\n        display: grid;\r\n        grid-template-columns: repeat(2, 1fr);\r\n        gap: 20px;\r\n        margin-top: 30px;\r\n    }\r\n    .card {\r\n        background-color: #1f1f1f;\r\n        padding: 20px;\r\n        border-radius: 8px;\r\n    }\r\n    .card h2 {\r\n        font-size: 1.5em;\r\n        margin-bottom: 10px;\r\n    }\r\n    .card p {\r\n        font-size: 1.1em;\r\n        color: #d4d4d4;\r\n    }')
    # Track blog page view server-side
    """Checks if user has an ID, creates one if not, and returns it"""
    user_id = session.get('user_id')
    if not user_id:
        user_id = str(uuid.uuid4())
        session['user_id'] = user_id    
    
    posthog.capture('blog_page_viewed', distinct_id=user_id)
    
    return Html(
    head,
    Body(
        header,
        Main(
            Section(
                Div(
                    H1('DivergenceAI Blog'),
                    P('Stay up-to-date with the latest news, insights, and advancements in electromagnetic simulation.'),
                    cls='container'
                ),
                cls='blog-hero'
            ),
            Section(
                Div(
                    Article(
                        H2('What If Running Simulations Was as Easy as Chatting with AI?'),
                        Div(
                            Span('April 9th, 2025', cls='date'),
                            Span('by Gustavo Navarro', cls='author'),
                            cls='post-meta'
                        ),
                        P('We don’t just want better tools — we need them to bring ideas to life faster. But what does “better” actually look like?'),
                        A('Read More', href='https://www.linkedin.com/pulse/what-running-simulations-easy-chatting-ai-gustavo-navarro-ljrpc', cls='btn btn-secondary'),
                        cls='blog-post'
                    ),
                    cls='container'
                ),
                cls='blog-posts'
            ),
            Section(
                Div(
                    Article(
                        H2('The Future of Open-Source Simulation - Bridging Accessibility and Performance'),
                        Div(
                            Span('March 6th, 2025', cls='date'),
                            Span('by Gustavo Navarro', cls='author'),
                            cls='post-meta'
                        ),
                        P('Open source, combined with AI-driven innovation, is making advanced engineering simulation tools more accessible, reducing costs and lowering adoption barriers for small and mid-sized companies.'),
                        A('Read More', href='https://www.linkedin.com/pulse/future-open-source-simulation-bridging-performance-gustavo-navarro-dl0hc/?trackingId=GoRRqDv9QSK4po2kbuW88A%3D%3D', cls='btn btn-secondary'),
                        cls='blog-post'
                    ),
                    cls='container'
                ),
                cls='blog-posts'
            ),
            Section(
                Div(
                    Article(
                        H2('The Hidden Bottlenecks of RF and Antenna Simulations'),
                        Div(
                            Span('February 28, 2025', cls='date'),
                            Span('by Gustavo Navarro', cls='author'),
                            cls='post-meta'
                        ),
                        P('Simulation engineers are stuck battling clunky tools, long wait times, and broken workflows—AI automation can change that.'),
                        A('Read More', href='https://www.linkedin.com/pulse/hidden-bottlenecks-rf-antenna-simulations-gustavo-navarro-itijc/?trackingId=2FyXzuLcSYSrCpKi%2BRSioQ%3D%3D', cls='btn btn-secondary'),
                        cls='blog-post'
                    ),
                    cls='container'
                ),
                cls='blog-posts'
            ),
        ),
        footer,
        Script(src='animations.js')
    ),
)



# Add a new endpoint to handle the event capture
@app.post("/capture-event")
async def capture_event(session, request):
    data = await request.json()
    """Checks if user has an ID, creates one if not, and returns it"""
    user_id = session.get('user_id')
    if not user_id:
        user_id = str(uuid.uuid4())
        session['user_id'] = user_id    
    
    event_name = data.get('event')
    posthog.capture(
        event_name,
        distinct_id=user_id,
        properties={
            'email': data.get('email'),
            'has_request': bool(data.get('request'))
        }
    )
    return {"status": "success"}

serve()