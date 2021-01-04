let registros = []
function isDigitoMatricula() {
    const matricula = document.querySelector("#matricula")
    const nome = document.querySelector("#nome")
    if (matricula.value !== '') {
        nome.setAttribute('readonly', true)
    } else {
        nome.removeAttribute('readonly')
    }
}

function isDigitoNome() {
    const matricula = document.querySelector("#matricula")
    const nome = document.querySelector("#nome")
    if (nome.value !== '') {
        matricula.setAttribute('readonly', true)
    } else {
        matricula.removeAttribute('readonly')
    }
}

function pesquisar(event) {
    event.preventDefault()
    const url = 'http://localhost:4000/registros'

    const nome = document.querySelector("#nome").value
    const matricula = document.querySelector("#matricula").value
    const mes = document.querySelector("#mes").value
    const ano = document.querySelector("#ano").value

    const registros = document.querySelector('#registros')

    fetch(`${url}?matricula=${matricula}&mes=${mes}&ano=${ano}`)
        .then(response => response.json())
        .then(regs => {
            registros.innerHTML =
            `<table>
                <thead>
                    <tr>
                        <th>Dia da semana</th>
                        <th>Data</th>
                        <th>Entrada 1</th>
                        <th>Saida 1</th>
                        <th>Entrada 2</th>
                        <th>Saida 2</th>
                        <th>Entrada 3</th>
                        <th>Saida 3</th>
                        <th>Horas Trabalhadas</th>
                    </tr>
                </thead>
                <tbody>
                    ${regs.map(reg => !reg.totais ?
                    `<tr>
                        <td>${reg.dia_semana}</td>
                        <td>${reg.data}</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td>${reg.horas_trabalhadas}</td>
                    </tr>`: '').join('')}                    
                </tbody>
            </table>`
        })
        .catch(console.error)
}

(function getAnos() {
    let anos = []

    for (i=2010; i < new Date().getFullYear(); i++) {
        anos.push(i)
    }

    const selectAno = document.querySelector('#ano')
    selectAno.innerHTML = anos.map(ano => `<option value="${ano}">${ano}</option>`)
})()

// <td>${reg.horas[0] ? reg.horas[0] : ''}</td>
// <td>${reg.horas[1] ? reg.horas[1] : ''}</td>
// <td>${reg.horas[2] ? reg.horas[2] : ''}</td>
// <td>${reg.horas[3] ? reg.horas[3] : ''}</td>
// <td>${reg.horas[4] ? reg.horas[4] : ''}</td>
// <td>${reg.horas[5] ? reg.horas[5] : ''}</td>