function bruteDecodeContinuous() {
    // Function to send an AJAX request to the server and update the page
    function updatePage(data) {
        // Update the page content with the decoded text and best grids
        if (data.len != 0) {

            var bestDecodeText = data[0];
            var bestGrids = data[1];
            var bestScore = data[2];
            var currentIteration = data[3];
            
            document.getElementById("result-para").innerText = "Current Iteration: " + currentIteration.toString();

            var brute_force_table = document.getElementById('brute-force-table');
            var row = brute_force_table.insertRow(0);

            var grids_cell = row.insertCell(0);
            var decrypt_cell = row.insertCell(1);
            var fitness_cell = row.insertCell(2)
            
            grids_cell.classList.add("grids-td");
            decrypt_cell.classList.add("decrypt-td");
            fitness_cell.classList.add("fitnesss-td");

            var grids_table = document.createElement('table');
            for (var i = 0; i < 2; i++) {
                var row = grids_table.insertRow(i);
            
                for (var j = 0; j < 2; j++) {
                var cell = row.insertCell(j);
                var currentGrid = bestGrids[i * 2 + j];
                var nestedFiveByFiveGrid = document.createElement('table');
            
                for (var m = 0; m < 5; m++) {
                    var nestedRow = nestedFiveByFiveGrid.insertRow(m);
            
                    for (var n = 0; n < 5; n++) {
                    var nestedCell = nestedRow.insertCell(n);
                    nestedCell.textContent = currentGrid[m][n];
                    nestedCell.style.textAlign = "center";
                    }
                }
            
                cell.appendChild(nestedFiveByFiveGrid);
                };
            };
            grids_cell.appendChild(grids_table);

            decrypt_cell.innerText = bestDecodeText;
            fitness_cell.innerText = bestScore;

            // document.getElementById('result-para').innerText = "Best Decoded Text: " + data[0] + "\nBest Grids: " + data[1] + "\nBest Fitness: " + data[2];
    
        }
    }

    function makeRequest() {
        // Make an AJAX request to the server for the "brute_decode" operation
        fetch('/ciphers/four-square-cipher/brute-force', {
            method: 'GET',
            // headers: {
            //     'Content-Type': 'application/x-www-form-urlencoded',
            // },
            // body: new URLSearchParams({
            //     text: document.getElementById('text').value,
            //     grid_a: document.getElementById('grid_a').value,
            //     grid_b: document.getElementById('grid_b').value,
            //     grid_c: document.getElementById('grid_c').value,
            //     grid_d: document.getElementById('grid_d').value,
            //     operation: 'brute_decode',
            //     tight: document.getElementById('tight').value,
            //     alphabet: document.getElementById('alphabet').value,
            //     anp: document.getElementById('anp').value,
            //     min_length: document.getElementById('min_length').value,
            //     max_length: document.getElementById('max_length').value,
            // }),
        })
        .then(response => response.json())
        .then(data => updatePage(data))
        .catch(error => console.error('Error:', error));
    }
    setInterval(makeRequest, 1000);

}
document.getElementById('four-square-form').addEventListener('submit', function(event) {

    // Check if the operation is "brute_decode"
    if (document.getElementById('operation').value === 'brute_decode') {
        event.preventDefault();
        bruteDecodeContinuous();  // Start continuous update process
    }
});
// window.onload = bruteDecodeContinuous;
