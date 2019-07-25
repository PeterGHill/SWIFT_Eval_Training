def amplitude_SAL(obs,mod):

    #obs and mod are rainfall accumulation over a certain period and averaged over a certain domain
    #it could be good to calculate this for different accumulations

    return (mod-obs)/(0.5*(mod+obs))