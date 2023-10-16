def update_progress(iter:int,total:int,size:int=20):
    print("\033[F\033[K[" + "="*int(round(size*iter/total,0)) + " "*(size-int(round(size*iter/total, 0))) + "]" + f' {iter*100/total:.1f}%')