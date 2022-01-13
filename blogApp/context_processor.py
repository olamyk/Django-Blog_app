from foo import Configuration

def code_base(request):

    conf = Configuration.objects.all()
    print('my content processor ',conf)
    return {'conf':conf}