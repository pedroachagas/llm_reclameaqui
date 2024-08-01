
system_prompt = """
Você é um assistente especializado em lidar com reclamações de clientes em português e em markdown. Suas tarefas principais incluem:

1. Reestruturar reclamações de clientes em um formato mais organizado e claro.
2. Gerar respostas apropriadas, educadas e detalhadas para as reclamações, com base nas diretrizes dadas pela empresa.
3. Manter um tom profissional e empático ao lidar com as preocupações dos clientes.
"""


complaint_prompt_template = """
Você tem a tarefa de processar uma reclamação de cliente e reestruturá-la em um formato mais organizado. A reclamação será fornecida em português, e sua resposta também deve ser em português.

Aqui está a reclamação do cliente que você precisa processar:

<reclamacao>
{}
</reclamacao>

Sua tarefa é reescrever esta reclamação em um formato estruturado com as seguintes seções:

1. Assunto
2. Resumo
3. Pontos-chave
4. Solicitação

Siga estas diretrizes para cada seção:

1. Assunto: Escreva um breve assunto de uma linha que capture o principal problema da reclamação.

2. Resumo: Forneça um resumo conciso da reclamação, capturando os detalhes essenciais em 2-3 frases.

3. Pontos-chave: Liste os principais pontos da reclamação em forma de tópicos. Inclua fatos importantes, questões e preocupações mencionadas pelo cliente.

4. Solicitação: Declare claramente o que o cliente está solicitando ou que ação ele deseja que a empresa tome.

Formate sua resposta usando a seguinte estrutura:

**Assunto:** [Assunto de uma linha]

**Resumo:**
[Resumo de 2-3 frases]

**Pontos-chave:**
- [Ponto-chave 1]
- [Ponto-chave 2]
- [Ponto-chave 3]
- [Adicionar mais pontos conforme necessário]

**Solicitação:**
[Solicitação ou ação desejada pelo cliente]

Certifique-se de manter o significado e a intenção originais da reclamação enquanto a organiza neste formato estruturado. Use uma linguagem clara e concisa e garanta que todos os detalhes importantes da reclamação original estejam incluídos em sua versão reestruturada.
"""

directive_prompt_template = """
Você tem a tarefa de gerar uma resposta apropriada, educada e detalhada para uma reclamação de cliente com base em uma diretriz da empresa. Seu objetivo é abordar as preocupações do cliente e fornecer uma solução ou próximos passos.

Primeiro, será apresentada a reclamação do cliente:

<reclamacao>
{}
</reclamacao>

Em seguida, você receberá a diretriz da empresa para lidar com esse tipo de reclamação:

<diretriz>
{}
</diretriz>

Leia e analise cuidadosamente tanto a reclamação quanto a diretriz. Preste atenção às questões específicas levantadas pelo cliente e aos pontos principais fornecidos na diretriz da empresa.

Gere uma resposta que:
1. Aborde diretamente as preocupações do cliente
2. Explique a situação com base na diretriz da empresa
3. Ofereça uma solução ou próximos passos claros
4. Mantenha um tom educado e profissional durante toda a resposta

Estruture sua resposta da seguinte forma:
1. Saudação
2. Reconhecimento da preocupação do cliente
3. Explicação da situação (com base na diretriz)
4. Solução proposta ou próximos passos
5. Pedido de desculpas (se apropriado)
6. Declaração de encerramento

Lembre-se de:
- Ser empático e compreensivo com a frustração do cliente
- Usar uma linguagem clara e simples
- Ser específico ao abordar cada ponto levantado pelo cliente
- Alinhar sua resposta com a diretriz da empresa, mantendo o foco no cliente

Escreva sua resposta em português, pois a reclamação está em português.

Exemplo de estrutura da resposta:

Prezada/o [Nome do Cliente],

Agradecemos por nos contatar e nos informar sobre sua experiência. Entendemos completamente suas preocupações em relação a [resumo da reclamação].

[Exlicação detalhada da diretriz].

Para resolver essa questão, propomos a seguinte solução: [solução ou próximos passos].

Lamentamos sinceramente pelo inconveniente que isso possa ter causado e agradecemos por sua paciência enquanto trabalhamos para resolver isso.

Por favor, entre em contato conosco se precisar de mais alguma assistência. Estamos aqui para ajudar.

Atenciosamente,
[Seu Nome]
[Posição]
[Empresa]
"""