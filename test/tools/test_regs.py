def test_parse(t, g, regs):
    return {'test_regs':
        groov.Group('test_regs', [
            groov.Register('test', 0x0, [
                groov.Field('test', 'groov::w::replace', 0, 0)])])}
