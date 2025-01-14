from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ip-radius-source-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_radius_source_interfaces = resolve('ip_radius_source_interfaces')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='ip_radius_source_interfaces') if l_0_ip_radius_source_interfaces is missing else l_0_ip_radius_source_interfaces)):
        pass
        yield '\n### IP RADIUS Source Interfaces\n\n#### IP RADIUS Source Interfaces\n\n| VRF | Source Interface Name |\n| --- | --------------- |\n'
        for l_1_ip_radius_source_interface in t_2((undefined(name='ip_radius_source_interfaces') if l_0_ip_radius_source_interfaces is missing else l_0_ip_radius_source_interfaces)):
            _loop_vars = {}
            pass
            yield '| '
            yield str(t_1(environment.getattr(l_1_ip_radius_source_interface, 'vrf'), 'default'))
            yield ' | '
            yield str(environment.getattr(l_1_ip_radius_source_interface, 'name'))
            yield ' |\n'
        l_1_ip_radius_source_interface = missing
        yield '\n#### IP SOURCE Source Interfaces Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ip-radius-source-interfaces.j2', 'documentation/ip-radius-source-interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=30&10=33&11=37&17=43'