const labels = [
    '',
    '',
    '',
    '',
    '',
    '',
    '',
];

const data = {
    labels: labels,
    datasets: [{
        label: 'Anime mais visualizado',
        backgroundColor: [
            'rgb(255, 99, 132 )',
            'rgb(255, 159, 64 )',
            'rgb(255, 205, 86 )',
            'rgb(75, 192, 192 )',
            'rgb(54, 162, 235 )',
            'rgb(153, 102, 255 )',
            'rgb(201, 203, 207 )'
        ],
        borderColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 159, 64)',
            'rgb(255, 205, 86)',
            'rgb(75, 192, 192)',
            'rgb(54, 162, 235)',
            'rgb(153, 102, 255)',
            'rgb(201, 203, 207)'
        ],
        borderRadius: Number.MAX_VALUE,
        data: [314, 64, 44, 41, 35, 22, 22, 0],
    }]
};

const config = {
    type: 'bar',
    data: data,
    options: {
        options: {
            scales: {
                xAxes: [{
                    categoryPercentage: 0.5,
                    barPercentage: 0.3
                }],
                backdropPadding: {
                    x: 2,
                    y: 1
                }
            }
        }
    }
};