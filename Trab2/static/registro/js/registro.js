onload = function() {
    console.log('onload')
    // deveria ser change ou blur
    document.getElementById('id_username').addEventListener('keyup', verificaUsername);
    document.getElementById('id_password1').addEventListener('keyup', verificaPassword);
    document.getElementById('id_password2').addEventListener('keyup', verificaPasswordConfirmation);
  }
  
  //Verifica se o username digitado é único
  function verificaUsername(e) {
    console.log('verificaUsername')
    var campoUsername = document.getElementById('id_username');
    valorUsername = campoUsername.value;
    console.log('Campo username = ' + valorUsername)
    xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET',
      '/accounts/verificaUsername' + "?username=" + encodeURIComponent(valorUsername),
      true);
    xmlhttp.onreadystatechange = verificaUsernameCallBack;
    xmlhttp.send(null);
  }
  

  function verificaUsernameCallBack() {
    if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      var resposta = JSON.parse(xmlhttp.responseText)
      console.log(resposta)

      if(resposta.existe) {
        const div = document.getElementById("idErro");
        if(div.hasChildNodes()){
            div.removeChild(div.childNodes[0])
        }
        const text = document.createElement("span");
        text.innerHTML="Usuário já existe";
        div.appendChild(text);
        document.getElementById('id_username').style='border: 2px solid #FF0000;';
      }
      else {
        const div = document.getElementById("idErro");
        if(div.hasChildNodes()){
            div.removeChild(div.childNodes[0])
        }
      }
    }
  }

  // Verifica se a senha digitada está de acordo com os padrões
  // Pelo menos 8 caracteres com pelo menos uma letra
  function verificaPassword(e){
    var campoPassword = document.getElementById('id_password1');
    valorPassword = campoPassword.value;

    xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET',
      '/accounts/verificaPassword' + "?password=" + encodeURIComponent(valorPassword),
      true);
    xmlhttp.onreadystatechange = verificaPasswordCallBack;
    xmlhttp.send(null);

  }

  function verificaPasswordCallBack() {
    if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      var resposta = JSON.parse(xmlhttp.responseText)
      console.log(resposta)
      const div = document.getElementById("idErroPw");

      if(!resposta.valido) {
        if(div.hasChildNodes()){
          div.removeChild(div.childNodes[0])
        }

        const text = document.createElement("span");
        text.innerHTML="Senha não atende os padrões necessários";
        div.appendChild(text);
      } else {
        if(div.hasChildNodes()){
          div.removeChild(div.childNodes[0])
        }
      }
    }
  }

  // Verifica se a confirmação da senha é igual a senha
  function verificaPasswordConfirmation(e){
    var campoPassword = document.getElementById('id_password1');
    valorPassword = campoPassword.value;
   
    var campoPasswordConfirmation = document.getElementById('id_password2');
    valorPasswordConfirmation = campoPasswordConfirmation.value;

    xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET',
      '/accounts/verificaPasswordConfirmation' + "?password=" +  encodeURIComponent(valorPassword) + "&passwordConfirmation=" + encodeURIComponent(valorPasswordConfirmation)  ,true);
    xmlhttp.onreadystatechange = verificaPasswordConfirmationCallBack;
    xmlhttp.send(null);

  }


  function verificaPasswordConfirmationCallBack() {
    if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      var resposta = JSON.parse(xmlhttp.responseText)
      console.log(resposta)
      const div = document.getElementById("idErroPw");

      if(!resposta.same) {
        if(div.hasChildNodes()){
          div.removeChild(div.childNodes[0])
        }

        const text = document.createElement("span");
        text.innerHTML="Senhas não coincidem";
        div.appendChild(text);
      } else {
        if(div.hasChildNodes()){
          div.removeChild(div.childNodes[0])
        }
      }
    }
  }


  