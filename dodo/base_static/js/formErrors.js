
djangoErrorNode = document.querySelector('ul')
djangoErrorNode.style.display = 'none'

let errors = []
function getError(value){
    if (value.children.length > 0) {
        Array.from(value.children).forEach(function(val) {
            getError(val)
        })
    } else {
        errors.push(value.innerText)
    }
    return errors
}


function addFormErrorsToHTML(errors, errorClass, formClass) {
    form = document.querySelector(`.${formClass}`)
    node = document.querySelector(`.${errorClass}`)
    if(node && form) {
        errors.forEach(error => {
            errorTag = document.createElement('p')
            errorTag.innerText = error
            errorTag.style.color = "red"
            form.insertBefore(errorTag, node)
        }
    )} else {
        throw `Не найден элемент с классом ${errorClass} или форма с классом ${formClass}`
    }
}

errors_list = getError(djangoErrorNode)
addFormErrorsToHTML(errors_list, 'form_errors', 'form')