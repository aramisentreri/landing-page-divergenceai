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
        Link(rel='stylesheet', href='styles.css')
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
                    Span('DivergenceAI'),
                    href='/',
                    cls='logo'
                ),
                Nav(
                    A('Features', href='#features'),
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
                        H1(
                            Span('AI-powered Automation', cls='text-white'),
                            Span('for', cls='text-white'),
                            Span('Engineering Simulations', cls='gradient-text-purple'),
                        ),
                        P('Use AI to revolutionize physics simulation, empowering engineers, designers, and entrepreneurs with faster, more accessible, and more powerful tools.'),
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
                Div(
                    H2('Key Benefits'),
                    Div(
                        Div(
                            H3('Accelerated Design Iterations'),
                            P('Reduce simulation time by up to 80%, allowing for rapid prototyping and design optimization.'),
                            cls='benefit-card'
                        ),
                        Div(
                            H3('Improved Accuracy'),
                            P('Achieve higher precision in complex electromagnetic scenarios, leading to better product performance.'),
                            cls='benefit-card'
                        ),
                        Div(
                            H3('Cost-Effective Solutions'),
                            P('Minimize the need for physical prototypes, saving time and resources in the development process.'),
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
                    H2('Advanced Features'),
                    Div(
                        Div(
                            H3('Physics-Informed Neural Networks'),
                            P('Our tool leverages cutting-edge physics-informed neural networks to provide accurate and efficient electromagnetic simulations.'),
                            Ul(
                                Li('Faster convergence in complex scenarios'),
                                Li('Improved accuracy in multi-scale problems'),
                                Li('Seamless integration of physical constraints')
                            )
                        ),
                        Div(
                            Canvas(id='neuralNetworkCanvas'),
                            cls='animation-container'
                        ),
                        cls='features-grid'
                    ),
                    cls='container'
                ),
                id='features'
            ),
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

serve()