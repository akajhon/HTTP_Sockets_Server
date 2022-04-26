
    function sendPUTRequest() {
        let xhr = new XMLHttpRequest();
        event.preventDefault()
        let caminho = document.getElementById("caminho").value
        console.log(caminho)
        let url = "/" + caminho + ".txt"
        let button = document.getElementById("button");
        let arquivo = toString(document.getElementById("conteudo"))
        xhr.open("PUT", url, true);
        xhr.setRequestHeader("Content-Type", "text/plain");
        xhr.setRequestHeader("Cache-Control", "no-cache, no-store, max-age=0");
        xhr.send(arquivo);
        console.log("send: ", arquivo);
    }

    function sendPOSTRequest() {
        let xhr = new XMLHttpRequest();
        event.preventDefault()
        let caminho = document.getElementById("caminho").value
        console.log(caminho)
        let url = "/" + caminho + ".txt"
        let button = document.getElementById("button");
        let arquivo = toString(document.getElementById("conteudo"))
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "text/plain");
        xhr.setRequestHeader("Cache-Control", "no-cache, no-store, max-age=0");
	xhr.send(arquivo);
        console.log("send: ", arquivo);
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
    }
	
    xhr.onreadystatechange = function () {
	switch (this.readyState) {
        case 1:
            button.style.opacity = "1.0"
            button.setAttribute("disabled", "true");
            console.log("OPENED")
            break;
        case 4:
            if (this.status === 201) {
                button.style.backgroundColor = "#48D40B"
                button.innerText = "OK";
            } else {
                button.style.backgroundColor = "#EB1C0A"
                button.innerText = "ERROR"
            }

            setTimeout(() => {
                button.style.background = oldButtonColor;
                button.innerText = oldButtonName;
                button.removeAttribute("disabled");
            }, 1000)

            console.log("DONE")
            break;
            }
        }
