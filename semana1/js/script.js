const element = element => document.querySelector(element)
let pedido = null
let fieldNome = false
let fieldEndereco = false

element('div.btn1').onclick = () => {
    window.alert("Você escolheu Churrasco!")
    pedido = 'Churrasco'
}

element('div.btn2').onclick = () => {
    window.alert("Você escolheu Pão!")
    pedido = 'Pão'
}

element('div.btn3').onclick = () => {
    window.alert("Você escolheu Pizza!")
    pedido = 'Pizza'
}

element("input#name").addEventListener('keyup', () => {
    if(element("input#name").value === "")
        fieldNome = false
    else
        fieldNome = true

    if( fieldNome && fieldEndereco)
        element('form button').removeAttribute('disabled')
    else
        element('form button').setAttribute('disabled', "")
})

element("input#addr").addEventListener('keyup', () => {
    if(element("input#addr").value === "")
        fieldEndereco = false
    else
        fieldEndereco = true

    if( fieldNome && fieldEndereco)
        document.querySelector('form button').removeAttribute('disabled')
    else
        element('form button').setAttribute('disabled',"")
})


document.querySelector('form button').onclick = () => {
    window.alert('Enviado com sucesso!')
    window.location.href('localhost:5500/semana2/index.html')
} 