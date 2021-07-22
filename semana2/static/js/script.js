const cmd = element => document.querySelector(element)
const cmdAll = element => document.querySelectorAll(element)

cmdAll('div.area ul li').forEach( item => item.addEventListener('click', () => {
    if(item.classList.contains('risq'))
        item.classList.remove('risq')
    else
        item.classList.add('risq')
}))
