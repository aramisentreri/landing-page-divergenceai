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
        Script(src='https://polyfill.io/v3/polyfill.min.js?features=es6'),
        Script("""
        window.MathJax = {
          tex: {
            inlineMath: [['\\\\(', '\\\\)'], ['$', '$']],
            displayMath: [['\\\\[', '\\\\]'], ['$$', '$$']],
            processEscapes: true,
            processEnvironments: true
          },
          options: {
            ignoreHtmlClass: 'tex2jax_ignore',
            processHtmlClass: 'tex2jax_process'
          },
          startup: {
            pageReady: function () {
              return MathJax.startup.defaultPageReady().then(function () {
                // Function to fix math elements styling
                function fixMathStyling() {
                  var mathElements = document.querySelectorAll('.math-symbol mjx-container, .math-symbol .MathJax, #logo-math mjx-container, #logo-math .MathJax');
                  mathElements.forEach(function(elem) {
                    elem.style.webkitTextFillColor = '#c084fc';
                    elem.style.color = '#c084fc';
                    elem.style.background = 'none';
                    elem.style.webkitBackgroundClip = 'initial';
                    elem.style.opacity = '1';
                    elem.style.visibility = 'visible';
                  });
                }
                
                // Apply immediately
                setTimeout(fixMathStyling, 10);
                
                // Also apply after a short delay in case of timing issues
                setTimeout(fixMathStyling, 100);
                
                // Set up a mutation observer to catch any dynamically added math elements
                if (typeof MutationObserver !== 'undefined') {
                  var observer = new MutationObserver(function(mutations) {
                    mutations.forEach(function(mutation) {
                      if (mutation.addedNodes.length > 0) {
                        setTimeout(fixMathStyling, 10);
                      }
                    });
                  });
                  observer.observe(document.body, { childList: true, subtree: true });
                }
              });
            }
          }
        };
        """, type="text/javascript"),
        Script(src='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js', async_=True),
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
                    
                    H1(
                        Span('\\( \\nabla \\cdot \\)', id='logo-math', cls='math-symbol'), 
                        Span(' AI', cls='logo-text'), 
                        style='display: inline-block; margin-right: 2rem;'
                    ),
                    H2(Span('DivergenceAI'), style='display: inline-block; margin-right: 1rem;'),
                    href='/',
                    cls='logo'
                ),
                Nav(
                    A('How it Works', href='#workflows'),
                    A('Benefits', href='#benefits'),
                    A('See Demo', href='#product-demo'),
                    A('Pricing', href='#pricing'),
                    A(Button('Start Free Trial', cls='btn btn-primary'), href='https://dashboard.app.divergenceai.xyz')
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

    # --- YouTube Video Setup for Modal ---
    # youtube_video_id = "6Jn3-z7b1Xw"
    youtube_video_id = "iBEnF-fQWZw"
    # Modal video parameters - with controls for user interaction
    youtube_embed_url = f"https://www.youtube.com/embed/{youtube_video_id}?controls=1&modestbranding=1"#&start=33&end=166"

    demo_video_iframe = Iframe(
        src=youtube_embed_url,
        title="DivergenceAI Product Demo",
        frameborder="0",
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share",
        allowfullscreen=True,
        cls="demo-modal-iframe"
    )
    # --- End YouTube Video Setup ---


    return Html(
        head,
        Body(
            header,
            Main(
                Section(
                    Div(
                        Div(
                            Div('Automate HFSS Workflows with AI', cls='hero-title'),
                            P('With DivergenceAI, RF and Antenna engineers can generate and execute simulation workflows across Ansys HFSS, allowing teams to ship designs faster than ever.', cls='hero-subtitle'),
                            Div(
                                Div('🚀 Ship designs 10x faster', cls='hero-benefit'),
                                Div('🔄 Rapid Design Insight & Exploration', cls='hero-benefit'), 
                                Div('🎯 No HFSS migration needed', cls='hero-benefit'),
                                cls='hero-benefits'
                            ),
                            Div(
                                A(Button('Start Free Trial', cls='btn btn-primary btn-large'), href='https://dashboard.app.divergenceai.xyz', onclick='simpleEventCapture("hero_cta_clicked")'),
                                A(Button('Watch Demo', cls='btn btn-secondary btn-large'), href='#', onclick='showDemoModal()'),
                                cls='hero-cta-buttons'
                            ),
                            cls='hero-content'
                        ),
                        cls='container'
                    ),
                    
                    # Demo Video Modal
                    Div(id='demoOverlay', onclick='closeDemoModal()', cls='overlay demo-overlay'),
                    Div(
                        Button('X', onclick='closeDemoModal()', cls='close-btn'),
                        demo_video_iframe,
                        id='demoModal',
                        cls='modal demo-modal'
                    ),
                cls='hero'
            ),
            # Section(
            #     Div(
            #         P('Trusted by engineers at leading companies', cls='social-proof-subtitle'),
            #         Div(
            #             Div('🏢 Fortune 500', cls='customer-logo'),
            #             Div('🎓 Universities', cls='customer-logo'),
            #             Div('🚀 Startups', cls='customer-logo'),
            #             Div('🔬 Research Labs', cls='customer-logo'),
            #             cls='customer-logos'
            #         ),
            #         Div(
            #             Div(
            #                 P('"DivergenceAI reduced our simulation setup time from 3 weeks to 2 days. The AI debugging feature alone saved us countless hours of troubleshooting."'),
            #                 Div(
            #                     Strong('Dr. Sarah Chen'),
            #                     Br(),
            #                     Span('Senior RF Engineer, TechCorp', cls='testimonial-company'),
            #                     cls='testimonial-author'
            #                 ),
            #                 cls='testimonial-card'
            #             ),
            #             Div(
            #                 P('"The natural language interface makes complex simulations accessible to our entire team, not just the experts. Game-changing for our workflow."'),
            #                 Div(
            #                     Strong('Mike Rodriguez'),
            #                     Br(),
            #                     Span('Engineering Manager, InnovateLab', cls='testimonial-company'),
            #                     cls='testimonial-author'
            #                 ),
            #                 cls='testimonial-card'
            #             ),
            #             cls='testimonials-grid'
            #         ),
            #         cls='container'
            #     ),
            #     cls='social-proof'
            # ),
            Section(
                H1('Why HFSS Workflows Slow Engineers Down'),
                Div(
                    Div(
                        H2('Manual Mesh Generation'),
                        P('Engineers spend days tweaking mesh settings, material properties, and boundary conditions for each HFSS simulation—repetitive work that blocks innovation.'),
                        cls='card'
                    ),
                    Div(
                        H2('One-at-a-Time Testing'),
                        P('HFSS forces sequential scenario exploration. Testing design variations takes weeks when it should take hours—slowing time-to-market.'),
                        cls='card'
                    ),
                    Div(
                        H2('Simulation Expertise Bottleneck'),
                        P('Only senior engineers can effectively set up complex HFSS models, creating dependencies and limiting team scalability.'),
                        cls='card'
                    ),
                    Div(
                        H2('Disconnected CAD-to-Results'),
                        P('Manual CAD import, geometry cleanup, and post-processing creates gaps where errors multiply and insights get lost.'),
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
                        Div(
                            H1('Traditional HFSS Workflow', cls='workflows-title-muted'),
                            Div(
                                    H2('CAD Import & Cleanup'),
                                    P('Manually import geometry into HFSS, fix CAD issues, and simplify complex models for simulation readiness.'),
                                    cls='workflow-step'
                            ),
                            Div(
                                    H2('Mesh Generation Setup'),
                                    P('Define mesh parameters, and convergence criteria. Requires expertise to balance accuracy vs. compute time.'),
                                    cls='workflow-step'
                            ),
                            Div(
                                    H2('Boundary Conditions & Materials'),
                                    P('Set radiation boundaries, material properties, and excitation ports. Slow and easy to misconfigure.'),
                                    cls='workflow-step'
                            ),
                            Div(
                                    H2('Solve & Debug'),
                                    P('Submit HFSS analyze and wait hours/days withuot supervision. When it fails (often), debug mesh, convergence, or setup issues manually.'),
                                    cls='workflow-step'
                            ),
                            Div(
                                    H2('Post-Process Results'),
                                    P('Extract S-parameters, field plots, and performance metrics. Repeat entire process for each design variation.'),
                                    cls='workflow-step'
                            ),
                            cls='workflow-column'
                        ),
                        Div(
                            H1('AI-Automated HFSS Workflow', cls='workflows-title'),
                            Div(
                                Div(
                                    H2('Intelligent CAD-to-HFSS'),
                                    P('AI automatically imports, cleans, and optimizes your CAD geometry for HFSS. Generates simulation-ready mesh settings without expert tuning.'),
                                    cls='workflow-step'
                                ),
                                Div(
                                    H2('Autonomous Simulation Management'),
                                    P('AI monitors HFSS jobs, detects convergence issues, and auto-adjusts settings. Get reliable results without manual debugging or restarts.'),
                                    cls='workflow-step'
                                ),
                                Div(
                                    H2('Post-Processing & Scenario Exploration'),
                                    P('Automatically extract key insights from your HFSS simulations in minutes instead of hours — S-parameters, field data, and performance metrics. Compare design scenarios with natural language requests and make engineering decisions faster.'),
                                    cls='workflow-step'
                                ),
                            ),
                        cls='workflow-column'
                        ),
                    cls='workflow-container'
                    ),
                cls='workflows',
                id='workflows'
                ),
            ),
            Section(
                Div(
                    H2('Scale HFSS Impact Without Increasing Headcount', cls='benefits-title'),
                    Div(
                        Div(
                            H3('Deploy AI Agents Across HFSS'),
                            P('Automate repetitive tasks across your HFSS workflow—from CAD to insights report—so engineers can focus on high-value design decisions.'),
                            Div('Impact: Accelerate post-processing and design iteration', cls='roi-metric'),
                            cls='benefit-card'
                        ),
                        Div(
                            H3('Parallel Scenario Exploration'),
                            P('Run multiple design variations simultaneously across HFSS instances. Compare antenna performance and optimize matching networks more efficiently.'),
                            Div('Impact: Faster evaluation of design alternatives', cls='roi-metric'),
                            cls='benefit-card'
                        ),
                        Div(
                            H3('No HFSS Migration Required'),
                            P('Enhance your existing HFSS workflows with AI automation—no retraining or process changes required.'),
                            Div('Impact: Immediate value with zero migration risk', cls='roi-metric'),
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
                    H2('See DivergenceAI in Action', cls='product-demo-title'),
                    P('From CAD upload to insights in minutes—watch how our platform transforms simulation workflows.', cls='product-demo-subtitle'),
                    Div(
                        Div(
                            H3('Upload & AI-Driven Geometry'),
                            P('Create HFSS geometries instantly with natural language requests. Just describe the shapes you need, and our AI generates the corresponding geometric primitives for you—no manual CAD work required.'),
                            Img(src='media/pre_processing_geometry.png', alt='CAD Generation', cls='demo-screenshot', onclick='showImageModal("media/pre_processing_geometry.png", "CAD Upload Interface")'),
                            cls='demo-step'
                        ),
                        Div(
                            H3('Simulation Control & Monitoring'),
                            P('Run simulations and parameter sweeps directly through natural language commands. Track progress in real time with live status updates, and let AI handle common issues before they cause failures. Schedule post-simulation actions like email notifications, S-parameter extraction, and field plot generation—so results are ready the moment your run finishes.'),
                            Img(src='media/hfss_app_sim_monitoring.png', alt='Simulation Agent', cls='demo-screenshot', onclick='showImageModal("media/hfss_app_sim_monitoring.png", "Simulation Dashboard")'),
                            cls='demo-step'
                        ),
                        Div(
                        H3('AI-Powered Results Visualization'),
                        P('Quickly explore your simulation results with natural language. Generate S-parameter plots, Smith charts, or far-field radiation patterns on demand—without writing a single script.'),
                        Img(src='media/app_hfss_variations_s11.png', alt='Simulation Results Visualization', cls='demo-screenshot', onclick='showImageModal("media/app_hfss_variations_s11.png", "Simulation Results Visualization")'),
                        cls='demo-step'
                    ),
                    Div(
                        H3('New: Automated Antenna Array Design'),
                        P('Automated beam steering and sidelobe control, with automatic data capture, six tapering algorithms (Chebyshev, Taylor, cosine, and more), and instant performance validation tools.'),
                        Img(src='media/app_hfss_beam_steering.png', alt='Array Design', cls='demo-screenshot', onclick='showImageModal("media/app_hfss_beam_steering.png", "Array Design Automation")'),
                        cls='demo-step'
                    ),
                        cls='demo-steps-grid'
                    ),
                    cls='container'
                ),
                cls='product-demo',
                id='product-demo'
            ),
            Section(
                Div(
                    H2('Pricing Plans', cls='pricing-title'),
                    P('Choose the plan that fits your workflow. Start with a trial or contact us for enterprise options.', cls='pricing-subtitle'),
                    Div(
                        Div(
                            H3('Professional', cls='tier-title'),
                            Div('$99', cls='tier-price'),
                            P('per month', cls='tier-period'),
                            Ul(
                                Li('Access to HFSS Copilot core features'),
                                Li('Automated post-processing (plotting, reporting, beam steering, sidelobe control, etc.)'),
                                Li('Unlimited projects & saved configurations'),
                                Li('Email support & setup tutorials'),
                                Li('Export results for further analysis'),
                                cls='tier-features'
                            ),
                            P(
                                'Best for individual engineers and small teams who want to speed up antenna array workflows and reduce manual post-processing time.',
                                cls='tier-description'
                            ),
                            Div(
                                P('💼 Great for RF engineers and consultants.', cls='tier-badge'),
                                A(Button('Start Pro Trial', cls='tier-btn tier-btn-pro'), href='https://dashboard.app.divergenceai.xyz', onclick='simpleEventCapture("pro_tier_clicked")'),
                                cls='tier-footer'
                            ),
                            cls='pricing-tier professional-tier'
                        ),
                        Div(
                            H3('Enterprise', cls='tier-title'),
                            Div('Custom', cls='tier-price-contact'),
                            P('pricing', cls='tier-period'),
                            Ul(
                                Li('Everything in Professional'),
                                Li('Private deployments or on-premises integration'),
                                Li('Enhanced data isolation & encryption'),
                                Li('Custom workflows and automation features'),
                                Li('Priority support & roadmap input'),
                                cls='tier-features'
                            ),
                            P(
                                'For companies with strict security requirements or larger teams. Includes private deployment options, enterprise data controls, and direct support.',
                                cls='tier-description'
                            ),
                            Div(
                                P("🛡️ Flexible pricing based on your team’s scale and security needs.", cls='tier-badge'),
                                Button('Contact Sales', onclick='showContactModal()', cls='tier-btn tier-btn-enterprise'),
                                cls='tier-footer'
                            ),
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
                
                # Image Modal for expanded view
                Div(id='imageOverlay', onclick='closeImageModal()', cls='overlay image-overlay'),
                Div(
                    Button('X', onclick='closeImageModal()', cls='close-btn'),
                    Img(id='expandedImage', cls='expanded-image'),
                    P(id='imageCaption', cls='image-caption'),
                    id='imageModal',
                    cls='modal image-modal'
                ),
                id='pricing'
            ),
            Section(
                Div(
                    H2('Built for Enterprise HFSS Workflows', cls='trust-title'),
                    Div(
                        Div(
                            H3('🔒 IP Protection & Data Security'),
                            P('Runs inside your secure environment, with support for enterprise encryption and isolated compute.'),
                            cls='trust-item'
                        ),
                        Div(
                            H3('⚡ HFSS-Native Integration'),
                            P('Uses official Ansys HFSS APIs and licensing to ensure compatibility without hacks or reverse engineering.'),
                            cls='trust-item'
                        ),
                        Div(
                            H3('🎯 Validated by RF Teams'),
                            P('Developed and tested in collaboration with RF engineers across aerospace, telecom, and advanced hardware companies.'),
                            cls='trust-item'
                        ),
                        Div(
                            H3('🏆 RF Engineering Expertise'),
                            P('Founded by PhDs in electromagnetics with expertise in partial differential equations and RF systems engineering, with deep technical foundations from UC Davis and Georgia Tech, and industry experience developing RF technologies and scaling engineering teams at companies including Apple.'),
                            cls='trust-item'
                        ),
                        cls='trust-grid'
                    ),
                    cls='container'
                ),
                cls='trust-section'
            ),
            Section(
                Div(
                    H2('Ready to Accelerate Your Simulations?'),
                    P('Join engineering teams saving 90% of their setup time with AI-powered simulation tools.'),
                    
                    Div(
                        Div(
                            H3('Start Your Free Trial'),
                            P('Experience the power of AI simulation with unlimited access for 14 days.'),
                            A(Button('Start Free Trial', cls='btn btn-primary btn-large'), href='https://dashboard.app.divergenceai.xyz'),
                            cls='cta-option'
                        ),
                        Div(
                            H3('Talk to Our Team'),
                            P('Get a personalized demo and discuss your specific simulation needs.'),
                            Button('Schedule Demo', onclick='showContactModal()', cls='btn btn-secondary btn-large'),
                            cls='cta-option'
                        ),
                        cls='cta-options'
                    ),

                    Div(
                        P('✅ No credit card required'),
                        P('✅ Full feature access during trial'),
                        P('✅ Setup support included'),
                        cls='cta-benefits'
                    ),

                    cls='container',
                ),
                cls='cta',
                id='cta')
            ),
        footer,
        Script(src='app.js')
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
        Script(src='app.js')
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