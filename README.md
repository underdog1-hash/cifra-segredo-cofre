# cifra-segredo-cofre

Estudo de Caso: A Cifra do Segredo de Cofre (Combination Lock Cipher)\n
Autor: Elcana Pedro\n
Contexto: Notas de estudo sobre Criptografia Simétrica, Cifras de Fluxo e Análise de Vulnerabilidades.\n

1. Introdução e Intuição Mecânica\n

Ao estudar os conceitos de criptografia clássica, idealizei um sistema de criptografia simétrica baseado no funcionamento mecânico dos cofres de segredo giratório de 3 discos.A premissa baseia-se na evolução da Cifra de César: em vez de deslocar o alfabeto por um fator fixo estático, a cifra utiliza uma sequência de rotações que alternam o sentido (direita/esquerda) dentro de uma escala delimitada, gerando uma cifragem polialfabética dinâmica.

2. Abordagem de Design e Evolução Matemática\n
   
Fase 1: O Modelo Estático (Vigenère Numérico)A primeira abordagem utilizava uma tupla fixa de 3 números como chave (ex: (5, 12, 3)).Falha Estrutural: Comportamento idêntico à Cifra de Vigenère. O tamanho fixo da chave expõe o texto ao Ataque de Kasiski (análise de frequência em blocos repetidos a cada (N) caracteres). Além disso, o espaço de chaves de (26^3 = 17.576) combinações é trivial para ataques de força bruta modernos.\n\n

Fase 2: O Modelo Dinâmico de Fluxo (Gerador Pseudoaleatório)Para mitigar a previsibilidade sem destruir o determinismo necessário para a decifragem, o algoritmo foi evoluído para uma Cifra de Fluxo utilizando um Gerador Linear Congruencial (LCG) baseado em uma Progressão Aritmética (P.A.).\n\n

   A fórmula de transição de estado para cada caractere (n) é definida por:

   (X_{n}=(X_{n-1}+Razão)\ (mod12)}+1)

   O sentido do giro é determinado alternando o sinal algebricamente baseado na paridade do índice do caractere:

   Deslocamento = X_{n}\times (-1)^{n}

  \n\n A Vulnerabilidade da Escala Reduzida: Limitar a escala a (menor ou igual 12) gera apenas (12 times 12 = 144) estados de chaves iniciais possíveis. Adicionalmente, criptografar a mensagem múltiplas vezes em camadas (múltiplos giros) não resolve o problema, pois operações consecutivas de deslocamento alfabético sofrem de fechamento, reduzindo-se sempre a uma única operação equivalente de rotação.\n

3. Implementação Prática (Python)
   Verificar o src com o file python\n\n

4. Conclusão e Paralelo com Criptografia Assimétrica\n\n
   
Este experimento ilustra perfeitamente a barreira fundamental da criptografia simétrica: o gerenciamento seguro e a robustez do espaço de chaves.No cenário Simétrico Real: Para que esta ideia mecânica do cofre fosse considerada segura hoje, a nossa "equação geradora" precisaria operar em um espaço de estados massivo (como o algoritmo AES ou o gerador ChaCha20), onde a semente inicial possui (2^{256} combinações impossíveis de serem computadas por força bruta.O Contraste Assimétrico: Na criptografia assimétrica (como RSA ou ECC), nós abandonaríamos o conceito de "compartilhar o segredo do cofre". Em vez disso, o processo usaria funções matemáticas unidirecionais baseadas em problemas difíceis (fatoração de primos ou curvas elípticas), permitindo que qualquer pessoa "feche a porta do cofre" (chave pública), mas apenas o dono legítimo possua a geometria matemática exata para "abrir o cofre" (chave privada).
