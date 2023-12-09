async function sendData() {
    try {
        var url = "gradient";
        var data = {
            variables: document.getElementById("variables").value,
            function: document.getElementById("function").value,
            initialVector: document.getElementById("initialVector").value,
            learningRate: document.getElementById("learningRate").value,
            tolerance: document.getElementById("tolerance").value,
            maxIterations: document.getElementById("maxIterations").value,
        };

        var jsonData = JSON.stringify(data);

        var response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: jsonData
        });

        if (!response.ok) {
            alert("Falló de comunicación con el servidor.");
        }

        var response = await response.json();
        
        if (response.code == 0){
            p_result_vec = document.getElementById("resultVector");
            p_result_val = document.getElementById("resultValue");

            p_result_vec.innerHTML = response.result;
            p_result_val.innerHTML = response.value;
        }
        else if (response.code == 1)
            alert("Función mal definida.");
        else if (response.code == 2)
            alert("Parámetros mal definidos.");
        else
            alert("Error general.");

    } catch (error) {
        console.log(error);
        alert("Error general.");
    }
}