const labels = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Ago',
];

const data = {
    labels: labels,
    datasets: [{
        label: 'My First dataset',
        backgroundColor: 'rgb(1, 85, 141)',
        borderColor: 'rgb(1, 85, 141)',
        borderRadius: Number.MAX_VALUE,
        data: [42, 10, 5, 1, 2, 20, 30, 0],
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
                    x: 5,
                    y: 4
                }
            }
        }
    }
}