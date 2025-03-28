from fasthtml.common import *

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
        # Amplitude Analytics
        Script(src='https://cdn.amplitude.com/script/8066a231914fd92d214704b80926add5.js'),
        Script('window.amplitude.add(window.sessionReplay.plugin({sampleRate: 1}));window.amplitude.init(\'8066a231914fd92d214704b80926add5\', {"fetchRemoteConfig":true,"autocapture":true});')
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
                    A('Blog', href='/blog', cls='active'),
                    A(Button('Join the waitlist', cls='btn btn-primary'), href='#cta')
                ),
                cls='container'
            )
        )

footer = Footer(
            Div(
                P('© 2025 DivergenceAI. All rights reserved.'),
                cls='container'
            )
        )

@app.get("/")
def home():

    return Html(
        head,
        Body(
            header,
            Main(
                Section(
                    Canvas(id='emWaveCanvas'),
                    Div(
                        Div(
                            H1(Span('AI-powered Engineering Simulations'), cls='hero-h1'),
                            P('From CAD to insights in seconds. Streamline your workflow with AI—faster design cycles, smarter decisions, and seamless engineering.'),
                            # Form(
                            #     Input(type='hidden', name='access_key', value='af5f23cb-d08f-4578-b508-8ae2e3edd453'),
                            #     # Input(type='text', name='name', required=''),
                            #     Input(type='email', name='email', placeholder='Enter your email', required=''),
                            #     # Textarea(name='message', required=''),
                            #     Input(type='checkbox', name='botcheck', style='display: none;', cls='hidden'),
                            #     Button('Join the waitlist', type='submit', cls='btn btn-contact'),
                            #     Div(cls='result'),
                            #     method='POST',
                            #     id='heroForm'
                            # ),


                            # Wait list modal
                            Button('Join the Waitlist', onclick='showModal()', cls='waitlist-btn'),
                            Div(id='overlay', onclick='closeModal()', cls='overlay'),
                            Div(
                                Button('X', onclick='closeModal()', cls='close-btn'),
                                H3('Join the Waitlist'),
                                Label('Email:', fr='email'),
                                Input(type='hidden', name='access_key', id='access_key', value='af5f23cb-d08f-4578-b508-8ae2e3edd453'),
                                Input(type='email', id='email', required='', placeholder='Enter your email'),
                                Label('What would you like Divergence AI to do for you?', fr='request'),
                                Textarea(id='request', rows='4', required='', placeholder="Imagine this is DivergenceAI's input box, what would you ask it to do?"),
                                Button('Submit', onclick='submitForm()', cls='btn btn-contact'),
                                id='modal',
                                cls='modal'
                            ),
                            Div(cls='result', id='heroFormResult'),
                            cls='hero-content'
                        ),
                        cls='container'                  
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
                            H3('Automatic Preprocessing and Smart Meshing'),
                            P('Onboard geometry, simplify, iterate meshing, set up boundary conditions and simulation parameters.'),
                            cls='benefit-card'
                        ),
                        Div(
                            H3('Run Simulations with Autonomous Monitoring'),
                            P('Simulations often fail. Our monitoring agent detects issues in real-time, attempts to debug, and re-runs automatically to minimize downtime.'),
                            cls='benefit-card'
                        ),
                        Div(
                            H3('AI-Powered Postprocessing & Insights'),
                            P('Intuitive natural language interface allows users to interact with simulation results. The AI generates key visualizations, highlights insights, and enables easy sharing - making high-fidelity simulations more accessible to engineers.'),
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
                    H2('Ready to Transform Your Design Process?'),
                    P('Join the waitlist and be the first to see how DivergenceAI can revolutionize your simulations.'),
                    # Form(
                    #         Input(type='hidden', name='access_key', value='af5f23cb-d08f-4578-b508-8ae2e3edd453'),
                    #         # Input(type='text', name='name', required=''),
                    #         Input(type='email', name='email', placeholder='Enter your email', required=''),
                    #         # Textarea(name='message', required=''),
                    #         Input(type='checkbox', name='botcheck', style='display: none;', cls='hidden'),
                    #         Button('Join the waitlist', type='submit', cls='btn btn-contact'),
                    #         Div(cls='result'),
                    #         method='POST',
                    #         id='heroForm'
                    #     ),
                    # Wait list modal
                    Button('Join the Waitlist', onclick='showModal()', cls='waitlist-btn'),
                    Div(id='overlay', onclick='closeModal()', cls='overlay'),
                    Div(
                        Button('X', onclick='closeModal()', cls='close-btn'),
                        H3('Join the Waitlist'),
                        Label('Email:', fr='email'),
                        Input(type='hidden', name='access_key', id='access_key', value='af5f23cb-d08f-4578-b508-8ae2e3edd453'),
                        Input(type='email', id='email', required='', placeholder='Enter your email'),
                        Label('What would you like Divergence AI to do for you?', fr='request'),
                        Textarea(id='request', rows='4', required='', placeholder="Imagine this is DivergenceAI's input box, what would you ask it to do?"),
                        Button('Submit', onclick='submitForm()', cls='btn btn-contact'),
                        id='modal',
                        cls='modal'
                    ),
                    Div(cls='result', id='ctaFormResult'),

                    cls='container',
                    
                ),
                cls='cta',
                # id='cta'
            )
        ),
        footer,
        Script(src='animations.js')
    ),
    lang='en'
)
@app.get("/blog")
def blog():
    Style('.simulation-landscape {\r\n        font-family: Arial, sans-serif;\r\n        background-color: #0d0d0d;\r\n        color: white;\r\n        padding: 20px;\r\n        border-radius: 8px;\r\n    }\r\n    .simulation-landscape h1 {\r\n        font-size: 3em;\r\n        background: linear-gradient(90deg, #c084fc, #60a5fa);\r\n        -webkit-background-clip: text;\r\n        -webkit-text-fill-color: transparent;\r\n    }\r\n    .grid {\r\n        display: grid;\r\n        grid-template-columns: repeat(2, 1fr);\r\n        gap: 20px;\r\n        margin-top: 30px;\r\n    }\r\n    .card {\r\n        background-color: #1f1f1f;\r\n        padding: 20px;\r\n        border-radius: 8px;\r\n    }\r\n    .card h2 {\r\n        font-size: 1.5em;\r\n        margin-bottom: 10px;\r\n    }\r\n    .card p {\r\n        font-size: 1.1em;\r\n        color: #d4d4d4;\r\n    }')

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



@app.get("/join-waitlist")
def join_waitlist():

    return Form(
        Input(type='hidden', name='access_key', value='af5f23cb-d08f-4578-b508-8ae2e3edd453 '),
        Input(type='text', name='name', required=''),
        Input(type='email', name='email', required=''),
        Textarea(name='message', required=''),
        Input(type='checkbox', name='botcheck', style='display: none;', cls='hidden'),
        Button('Submit Form', type='submit'),
        action='https://api.web3forms.com/submit',
        method='POST'
    )


@app.get("/test")
def test():

    return Html(
    Head(
        Meta(charset='UTF-8'),
        Meta(name='viewport', content='width=device-width, initial-scale=1.0'),
        Title('Simulation Workflow'),
        Style('body {\r\n            font-family: Arial, sans-serif;\r\n            background-color: #111;\r\n            color: #fff;\r\n            display: flex;\r\n            justify-content: center;\r\n            align-items: center;\r\n            height: 100vh;\r\n            margin: 0;\r\n        }\r\n        .container {\r\n            display: flex;\r\n            gap: 50px;\r\n        }\r\n        .workflow-column {\r\n            background-color: #222;\r\n            padding: 20px;\r\n            border-radius: 10px;\r\n            width: 300px;\r\n        }\r\n        h1 {\r\n            background: linear-gradient(90deg, #c471ed, #12c2e9);\r\n            -webkit-background-clip: text;\r\n            color: transparent;\r\n            font-size: 2rem;\r\n        }\r\n        .step {\r\n            display: flex;\r\n            align-items: flex-start;\r\n            gap: 10px;\r\n            margin-bottom: 20px;\r\n        }\r\n        .step-number {\r\n            background-color: #444;\r\n            color: #fff;\r\n            padding: 10px;\r\n            border-radius: 50%;\r\n            width: 30px;\r\n            height: 30px;\r\n            display: flex;\r\n            justify-content: center;\r\n            align-items: center;\r\n            font-weight: bold;\r\n        }\r\n        .step-content h2 {\r\n            margin: 0;\r\n            font-size: 1.2rem;\r\n        }\r\n        .step-content p {\r\n            margin: 5px 0 0;\r\n            font-size: 0.9rem;\r\n            color: #ccc;\r\n        }')
    ),
    Body(
        Div(
            Div(
                H1('Traditional Simulation Workflow'),
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
                H1('New Simulation Workflow'),
                Div(
                    Div('1', cls='step-number'),
                    Div(
                        H2('Data Preparation'),
                        P('Automatically process geometry and setup conditions.'),
                        cls='step-content'
                    ),
                    cls='step'
                ),
                Div(
                    Div('2', cls='step-number'),
                    Div(
                        H2('AI-Powered Computation'),
                        P('Use AI models to accelerate simulations and reduce runtime.'),
                        cls='step-content'
                    ),
                    cls='step'
                ),
                Div(
                    Div('3', cls='step-number'),
                    Div(
                        H2('Real-Time Analysis'),
                        P('Instantly visualize and explore simulation results.'),
                        cls='step-content'
                    ),
                    cls='step'
                ),
                cls='workflow-column'
            ),
            cls='container'
        )
    ),
    lang='en'
)



serve()