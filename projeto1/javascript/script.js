// atalho padrão que uso para selecionar um elemento da DOM
const cmd = element => document.querySelector(element)

// ação relacionado ao botão de troca de humor
cmd('button').onclick = () => {
    let randint = Math.floor(Math.random() * (8 - 1) + 1) // função equivalente ao randint da biblioteca random do python
    cmd('img').src = humores[randint].img
    cmd('p.humor').innerHTML = humores[randint].humor
}

