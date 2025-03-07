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
        Script(src='https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js')
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
                            Form(
                                Input(type='hidden', name='access_key', value='af5f23cb-d08f-4578-b508-8ae2e3edd453'),
                                # Input(type='text', name='name', required=''),
                                Input(type='email', name='email', placeholder='Enter your email', required=''),
                                # Textarea(name='message', required=''),
                                Input(type='checkbox', name='botcheck', style='display: none;', cls='hidden'),
                                Button('Join the waitlist', type='submit', cls='btn btn-contact'),
                                Div(cls='result'),
                                method='POST',
                                id='heroForm'
                            ),
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
                Canvas(id='neuralNetworkCanvas'),
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
            # Section(
            #     Div(
            #         H2('Advanced Features'),
            #         Div(
            #             Div(
            #                 H3('Physics-Informed Neural Networks'),
            #                 P('Our tool leverages cutting-edge physics-informed neural networks to provide accurate and efficient electromagnetic simulations.'),
            #                 Ul(
            #                     Li('Faster convergence in complex scenarios'),
            #                     Li('Improved accuracy in multi-scale problems'),
            #                     Li('Seamless integration of physical constraints')
            #                 )
            #             ),
            #             Div(
            #                 Canvas(id='neuralNetworkCanvas'),
            #                 cls='animation-container'
            #             ),
            #             cls='features-grid'
            #         ),
            #         cls='container'
            #     ),
            #     id='features'
            # ),
            Section(
                Div(
                    H2('Ready to Transform Your Design Process?'),
                    P('Join the waitlist and be the first to see how DivergenceAI can revolutionize your simulations.'),
                    Form(
                            Input(type='hidden', name='access_key', value='af5f23cb-d08f-4578-b508-8ae2e3edd453'),
                            # Input(type='text', name='name', required=''),
                            Input(type='email', name='email', placeholder='Enter your email', required=''),
                            # Textarea(name='message', required=''),
                            Input(type='checkbox', name='botcheck', style='display: none;', cls='hidden'),
                            Button('Join the waitlist', type='submit', cls='btn btn-contact'),
                            Div(cls='result'),
                            method='POST',
                            id='heroForm'
                        ),
                    cls='container'
                ),
                # cls='cta',
                id='cta'
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
                        H2('The Hidden Bottlenecks of RF and Antenna Simulations'),
                        Div(
                            Span('February 28, 2025', cls='date'),
                            Span('by Gustavo Navarro', cls='author'),
                            cls='post-meta'
                        ),
                        P('Simulation engineers are stuck battling clunky tools, long wait times, and broken workflows—AI automation can change that.'),
                        A('Read More', href='/blog_hidden-bottlenecks-of-rf-and-antenna-simulations', cls='btn btn-secondary'),
                        cls='blog-post'
                    ),
                    cls='container'
                ),
                cls='blog-posts'
            )
        ),
        footer,
        Script(src='animations.js')
    ),
)

@app.get("/blog_hidden-bottlenecks-of-rf-and-antenna-simulations")
def blog_post():


    return Html(
        head,
        Body(
            header,
            Main(
                Article(
                H1('The Hidden Bottlenecks of RF and Antenna Simulations'),
                Div(
                    Span('February 28, 2025', cls='date'),
                    Span('by Gustavo Navarro', cls='author'),
                    cls='post-meta'
                ),
                Img(src='/placeholder.svg?height=400&width=800', alt='Physics-Informed Neural Networks Diagram', cls='article-image'),
                Div(
                    P("I've talked to dozens of RF, Antenna, and other simulation engineers in the last two months. Everyone is grappling with the same recurring issues—de-featuring geometries, running mesh studies, and constantly balancing complexity with simulation time."),
                    P("The frustration is palpable. Long wait times stall progress for days. One engineer told me, 'I'm completely blocked by the simulation time. I can't make any progress for days'. Another shared how devastating it is to 'wait 10 hours and then nothing. That's an entire day lost.' Imagine putting your best technical minds to work—only to have their momentum crushed by a failed simulation or, even worse, non-physical results."),
                    P("Tool integration—especially CAD imports—is another nightmare. Engineers often need mechanical CAD designs to integrate their antenna models, but the process is painful. 'Unless the mech e has done RF before, they export from CAD with 10,000 parts on it. The system is going to freak out'. Complex assemblies mean hours of manual clean-up just to get a usable model."),
                    P("The user interfaces of these tools add to the struggle. 'The tools are powerful, but they are not very user-friendly.' The steep learning curves slow new engineers down, while the older generation—holding much of the critical knowledge—is retiring, leaving massive skill gaps."),
                    P("As an avid open-source fan, I hoped these challenges would ease on the open-source side. Let this be your reality check: 'The problem with open source is that they don't have a GUI, so it's all scripting-based. For most engineers, it is too cumbersome'. This lack of user-friendly interfaces limits adoption, even when the underlying tech is solid. Worse, many engineers I spoke to don't trust open-source simulation tools as a true source of 'physics', which is why commercial tools market themselves as 'the gold standard for real physics'. Sound familiar?"),
                    P("So while open-source tools offer scripting flexibility and lower costs, only a limited number of engineers can truly leverage them. The frustration is real."),
                    P("All of this paints a clear picture: simulation engineers are stuck battling their tools instead of pushing the boundaries of what's possible. The most painful part? The technology to solve many of these problems already exists—just not in their field."),
                    P("Developer tools are advancing at light speed compared to simulation tools. Imagine a future where AI automation streamlines geometry preparation, meshing, material selection, boundary and initial conditions, simulation monitoring, and real-time debugging—all without an army of engineers or breaking the bank. It doesn't have to stay like this."),
                    P("It's time for true AI automation to come to this field, and I'm excited about it."),
                    P("DM me if you're interested in learning more."),
                    cls='article-content'
                ),
                cls='container'
            ),
            cls='article-page'
        ),
        footer,
        Script(src='animations.js')
    )
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