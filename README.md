# atividade-jokempo-rpc-ppd

### Aplicação desenvolvida em python criando uma função simples que simula um jogo de Pedra, Papel e Tesoura,
### aplicando os conceitos de Remote Procedure Call aprendidos na disciplina 
### de Programação Paralela e Distribuída.

```
    O jogo vai perguntar primeiro se você quer jogar contra a máquina ou contra outro jogador.


    Jogador contra NPC:
    Escolha a opção 1, ou seja, digite 1 no teclado e enter
    
    Escolha entre pedra (rock), papel (paper) ou tesoura (scissors)
    
    Digite no teclado a sua opção e enter, lembrando que:
    Rock > Scissors > Paper
    pedra ganha de tesoura, que ganha de papel, que ganha de pedra
    
    O NPC (máquina), vai escolher uma opção pseudo aleatória entre as três existentes

    No fim você vê o print do resultado na tela


    Jogador contra Jogador:
    Escolha a opção 2, ou seja, digite 2 no teclado e enter
    
    Escolha entre pedra (rock), papel (paper) ou tesoura (scissors)
    
    Digite no teclado a sua opção e enter, lembrando que:
    Rock > Scissors > Paper
    pedra ganha de tesoura, que ganha de papel, que ganha de pedra
    
    Se você foi o primeiro a jogar, a sua jogada vai ser registrada
    O servidor vai esperar outro jogador entrar
    Foi definido um tempo limite de espera de mais ou menos 30s

    Se você foi o segundo, a jogada do primeiro já está registrada
    O servidor vai registrar a sua jogada e comparar os resultados

    No fim você vê o print do resultado na tela
```