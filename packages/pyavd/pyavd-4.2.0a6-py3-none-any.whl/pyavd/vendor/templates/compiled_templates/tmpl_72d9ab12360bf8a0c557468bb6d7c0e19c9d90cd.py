from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/router-multicast.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_multicast = resolve('router_multicast')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast)):
        pass
        yield '!\nrouter multicast\n'
        if t_2(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4')):
            pass
            yield '   ipv4\n'
            def t_3(fiter):
                for l_1_rpf_route in fiter:
                    if t_2(environment.getattr(l_1_rpf_route, 'source_prefix')):
                        yield l_1_rpf_route
            for l_1_rpf_route in t_3(t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'rpf'), 'routes'), 'source_prefix')):
                _loop_vars = {}
                pass
                def t_4(fiter):
                    for l_2_destination in fiter:
                        if t_2(environment.getattr(l_2_destination, 'nexthop')):
                            yield l_2_destination
                for l_2_destination in t_4(t_1(environment.getattr(l_1_rpf_route, 'destinations'), 'nexthop')):
                    l_2_rpf_route_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_rpf_route_cli = str_join(('rpf route ', environment.getattr(l_1_rpf_route, 'source_prefix'), ' ', environment.getattr(l_2_destination, 'nexthop'), ))
                    _loop_vars['rpf_route_cli'] = l_2_rpf_route_cli
                    if t_2(environment.getattr(l_2_destination, 'distance')):
                        pass
                        l_2_rpf_route_cli = str_join(((undefined(name='rpf_route_cli') if l_2_rpf_route_cli is missing else l_2_rpf_route_cli), ' ', environment.getattr(l_2_destination, 'distance'), ))
                        _loop_vars['rpf_route_cli'] = l_2_rpf_route_cli
                    yield '      '
                    yield str((undefined(name='rpf_route_cli') if l_2_rpf_route_cli is missing else l_2_rpf_route_cli))
                    yield '\n'
                l_2_destination = l_2_rpf_route_cli = missing
            l_1_rpf_route = missing
            if t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'counters'), 'rate_period_decay')):
                pass
                yield '      counters rate period decay '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'counters'), 'rate_period_decay'))
                yield ' seconds\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'routing'), True):
                pass
                yield '      routing\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'multipath')):
                pass
                yield '      multipath '
                yield str(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'multipath'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'software_forwarding')):
                pass
                yield '      software-forwarding '
                yield str(environment.getattr(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'ipv4'), 'software_forwarding'))
                yield '\n'
        for l_1_vrf in t_1(environment.getattr((undefined(name='router_multicast') if l_0_router_multicast is missing else l_0_router_multicast), 'vrfs'), 'name'):
            _loop_vars = {}
            pass
            yield '   !\n   vrf '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_vrf, 'ipv4')):
                pass
                yield '      ipv4\n'
            if t_2(environment.getattr(environment.getattr(l_1_vrf, 'ipv4'), 'routing'), True):
                pass
                yield '         routing\n'
        l_1_vrf = missing

blocks = {}
debug_info = '2=24&5=27&7=30&8=37&9=45&10=47&11=49&13=52&16=56&17=59&19=61&22=64&23=67&25=69&26=72&29=74&31=78&32=80&35=83'