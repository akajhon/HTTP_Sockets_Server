    function toJSONString(form) {
        const obj = {};
        obj['recipe'] = document.getElementById("recipe").value
        return JSON.stringify(obj);
    }
    
    function sendPUTRequest() {
        let xhr = new XMLHttpRequest();
        event.preventDefault()
        let caminho = document.getElementById("caminho").value
        console.log(caminho)
        let url = "/" + caminho + ".txt"
        let button = document.getElementById("button");
        let arquivo = toJSONString(document.getElementById("conteudo"))
        xhr.open("PUT", url, true);
        xhr.setRequestHeader("Accept", "application/json");
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(arquivo);

        xhr.onreadystatechange = function () {
            if (xhr.status === 201) {
                alert("Operação Concluída com sucesso!\n" + xhr.status);
            }
            else{
                alert("Houve um erro durante a Operação!\n" + xhr.status);
            }
        };
    };
    
    function sendPOSTRequest() {
        let xhr = new XMLHttpRequest();
        event.preventDefault()
        let caminho = document.getElementById("caminho").value
        console.log(caminho)
        let url = "/" + caminho + ".txt"
        let button = document.getElementById("button");
        let arquivo = toJSONString(document.getElementById("conteudo"))
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Accept", "application/json");
        xhr.setRequestHeader("Content-Type", "application/json");	    
        xhr.send(arquivo);
        console.log("send: ", arquivo);
        
        xhr.onreadystatechange = function () {
            if (xhr.status === 200) {
                alert("Operação Concluída com sucesso!\n" + xhr.status);
            }
            else if (xhr.status === 201){
                alert("Operação Concluída com sucesso!\n" + xhr.status);
            }
            else{alert("Houve um erro durante a Operação!\n" + xhr.status);}
        };
    }

    function sendDELETERequest() {
        let xhr = new XMLHttpRequest();
        event.preventDefault()
        let caminho = document.getElementById("caminho").value
        console.log(caminho)
        let url = "/" + caminho + ".txt"
        let button = document.getElementById("button");
        let arquivo = toString(document.getElementById("conteudo"))
        xhr.open("DELETE", url, true);
        xhr.setRequestHeader("Content-Type", "text/plain");
        xhr.setRequestHeader("Cache-Control", "no-cache, no-store, max-age=0");
	    xhr.send(arquivo);
        console.log("send: ", arquivo);

        xhr.onreadystatechange = function () {
            if (xhr.status === 200) {
                alert("Operação Concluída com sucesso!\n" + xhr.status);
            }
            else{
                alert("Houve um erro durante a Operação!\n" + xhr.status);
            }
        };
    }