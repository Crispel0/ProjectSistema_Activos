

const registroTotales = [
        labels:["China", "EEUU", "Rusia", "Alemania", "India", "Brasil"],
        datasets:[{
            label: "registros totales",
            data: [],
            borderWidth: 1,
            borderColor: "#36A2EB",
            backgroundColor: [
              "rgb(0, 123, 177)",
              "rgb(74, 136, 162)",
              "rgb(176, 211, 228)",
              "rgb(250, 172, 130)",
              "rgb(187, 90, 44)",
              "rgb(127, 90, 44)",
            ],
          },
        ],
        options: {
            maintainAspectRation :false,
            responsive : true
        },
        options:{
            scales: {
              y: {
                beginAtZero: true
              }
            }
          }
]

const registroUsuarios = [
    labels:["China", "EEUU", "Rusia", "Alemania", "India", "Brasil"],
    datasets: [
      {
        label: "registro usuarios",
        data: [45e5, 25e4, 3e6, 24e6, 6e7, 15e5],
        borderWidth: 1,
        borderColor: "#36A2EB",
        backgroundColor: [
          "rgb(0, 123, 177)",
          "rgb(74, 136, 162)",
          "rgb(176, 211, 228)",
          "rgb(250, 172, 130)",
          "rgb(187, 90, 44)",
          "rgb(127, 90, 44)",
        ],
      }],
      options: {
        maintainAspectRation :false,
        responsive : true
    },
    options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
]

const registroActivos = [
    labels: ["China", "EEUU", "Rusia", "Alemania", "India", "Brasil"],
    datasets: [
      {
        label: "registro activos",
        data: [45e5, 25e4, 3e6, 24e6, 6e7, 15e5],
        borderWidth: 1,
        borderColor: "#36A2EB",
        backgroundColor: [
          "rgb(0, 123, 177)",
          "rgb(74, 136, 162)",
          "rgb(176, 211, 228)",
          "rgb(250, 172, 130)",
          "rgb(187, 90, 44)",
          "rgb(127, 90, 44)",
        ],
      }],
      options: {
        maintainAspectRation :false,
        responsive : true
    },
    options:{
        scales:{
          y:{
            beginAtZero: true
          }
        }
      }
]

const registroSoftware = [
    labels:["China", "EEUU", "Rusia", "Alemania", "India", "Brasil"],
    datasets: [
      {
        label: "registro software",
        data: [45e5, 25e4, 3e6, 24e6, 6e7, 15e5],
        borderWidth: 1,
        borderColor: "#36A2EB",
        backgroundColor: [
          "rgb(0, 123, 177)",
          "rgb(74, 136, 162)",
          "rgb(176, 211, 228)",
          "rgb(250, 172, 130)",
          "rgb(187, 90, 44)",
          "rgb(127, 90, 44)",
        ],
      }],
      options: {
        maintainAspectRation :false,
        responsive : true
    },
    options:{
        scales:{
          y:{
            beginAtZero: true
          }
        }
      }
]

const registroHardware = [
    labels: ["China", "EEUU", "Rusia", "Alemania", "India", "Brasil"],
    datasets: [{
        label: "poblacion paises",
        data: [],
        borderWidth: 2,
        borderColor: "#36A2EB",
        backgroundColor: [
          "rgb(0, 123, 177)",
          "rgb(74, 136, 162)",
          "rgb(176, 211, 228)",
          "rgb(250, 172, 130)",
          "rgb(187, 90, 44)",
          "rgb(127, 90, 44)"
        ]
      }],
    options:{
        maintainAspectRation: false,
        responsive: true,
    elements: {
        line: {
            borderWidth: 5
        }
        },
        options:{
            scales:{
                y:{
                    beginAtZero: true
                }
            }
        }
    }
]

renderGraph("graficos_totales", registroTotales,'doughnut')
renderGraph("grafico_usuarios", registroUsuarios,'bubble')
renderGraph("grafico_activos", registroActivos,'radar')
renderGraph("graficos_software", registroSoftware,'scatter')
renderGraph("grafico_hardware", registroHardware,'line')

  