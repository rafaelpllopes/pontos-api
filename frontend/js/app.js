let registros = []

const inputNome = document.querySelector("#input-nome")
const inputMatricula = document.querySelector("#input-matricula")
const selectAno = document.querySelector("#select-ano")
const selectMes = document.querySelector("#select-mes")
const nome = document.querySelector("#nome")
const matricula = document.querySelector("#matricula")
const mes = document.querySelector("#mes")
const ano = document.querySelector("#ano")
const fielRegistros = document.querySelector('#registros')
const profissionais = document.querySelector('#profissionais')

httpHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Request-Method': '*',
    'Access-Control-Request-Headers': '*',
    'Access-Control-Allow-Headers': '*'
}

const headers = new Headers(httpHeaders)

url_base = "http://192.168.50.21:4000"


function isDigitoMatricula() {
    if (inputMatricula.value !== '') {
        inputNome.setAttribute('readonly', true)
    } else {
        inputNome.removeAttribute('readonly')
    }
}

function isDigitoNome() {
    if (inputNome.value !== '') {
        inputMatricula.setAttribute('readonly', true)

        if (inputNome.value.length > 3) {

            mes.textContent = selectMes.value
            ano.textContent = selectAno.value

            const url = `${url_base}/profissionais/nome?nome=${inputNome.value}`

            fetch(url, { headers: headers })
                .then(res => res.json())
                .then(pro => {
                    profissionais.innerHTML = pro.map(p => `<ul class="list-group"><li class="list-group-item" onclick="selectProfissionais(${parseInt(p.matricula)})">${parseInt(p.matricula)} - ${p.nome}</li></ul>`).join('')
                })
        } else {
            profissionais.innerHTML = ''
        }

    }
}

function selectProfissionais(matricula) {
    trazMatricula(matricula)
    profissionais.innerHTML = ''
    fielRegistros.innerHTML = ''
}

function pesquisar(event) {
    event.preventDefault()
    const url = `${url_base}/registros`

    mes.textContent = selectMes.value
    ano.textContent = selectAno.value
    matricula.textContent = parseInt(inputMatricula.value)
    nome.textContent = inputNome.value

    fetch(`${url}?matricula=${inputMatricula.value}&mes=${selectMes.value}&ano=${selectAno.value}`, { headers: headers })
        .then(response => response.json())
        .then(regs => {
            fielRegistros.innerHTML = `
            <button class="btn btn-success btn-lg" id="imprimir" onclick="imprimir()">Imprimir</button>
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th scope="col">Dia da semana</th>
                        <th scope="col">Data</th>
                        <th scope="col">Entrada 1</th>
                        <th scope="col">Saida 1</th>
                        <th scope="col">Entrada 2</th>
                        <th scope="col">Saida 2</th>
                        <th scope="col">Entrada 3</th>
                        <th scope="col">Saida 3</th>
                        <th scope="col">Horas Trabalhadas</th>
                    </tr>
                </thead>
                <tbody>
                    ${regs.map(reg => !reg.totais ?
                `<tr>
                        <td>${reg.dia_semana}</td>
                        <td>${new Date(reg.data.split('-')).toLocaleDateString()}</td>
                        <td>${reg.horas[0] || '-'}</td>
                        <td>${reg.horas[1] || '-'}</td>
                        <td>${reg.horas[2] || '-'}</td>
                        <td>${reg.horas[3] || '-'}</td>
                        <td>${reg.horas[4] || '-'}</td>
                        <td>${reg.horas[5] || '-'}</td>
                        <td>${reg.horas_trabalhadas || '-'}</td>
                    </tr>`: '').join('')}                    
                </tbody>
                <tfoot>
                    <tr>
                        <th colspan="8">Total de Dias</th>
                        <td>${regs[regs.length - 1].totais.dias_registrados}</td>
                    </tr>
                    <tr>
                        <th colspan="8">Total de Registros:</th>
                        <td>${regs[regs.length - 1].totais.registros}</td>
                    </tr>
                </tfoot>
            </table>`
        })
}

(() => {
    let anos = []
    for (i = 2010; i <= new Date().getFullYear(); i++) {
        anos.push(i)
    }
    selectAno.innerHTML = anos.map(ano => `<option value="${ano}">${ano}</option>`)
})()

function imprimir() {
    window.print()
}

(() => {
    const mesAtual = new Date().getMonth() + 11
    selectAno.options[selectAno.options.length - 2].selected = true
    selectMes.options[mesAtual].selected = true
})()

function buscarMatricula() {
    mes.textContent = selectMes.value
    ano.textContent = selectAno.value

    if (inputMatricula) {
        trazMatricula(inputMatricula.value)
    }

}

function limpar(event) {
    event.preventDefault()
    fielRegistros.innerHTML = ''
    inputMatricula.value = ''
    inputNome.value = ''
    nome.textContent = ''
    matricula.textContent = ''
    mes.textContent = ''
    ano.textContent = ''
    inputNome.removeAttribute('readonly')
    // inputMatricula.removeAttribute('readonly')
    profissionais.innerHTML = ''
}

function trazMatricula(matricula) {
    const url = `${url_base}/profissionais/matricula/${matricula}`

    fetch(url, { headers: headers })
        .then(res => res.json())
        .then(pro => {
            inputNome.value = pro.nome
            inputMatricula.value = pro.matricula
            nome.textContent = pro.nome
            matricula.textContent = parseInt(pro.matricula)
        })
}