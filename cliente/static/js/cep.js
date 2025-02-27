$(document).ready(function() {
    function limpa_formulário_cep() {
        $("#id_logradouro").val("");
        $("#id_bairro").val("");
        $("#id_cidade").val("");
        $("#id_estado").val("");
    }
    
    $("#id_cep").blur(function() {
        var cep = $(this).val().replace(/\D/g, '');
        
        if (cep != "") {
            var validacep = /^[0-9]{8}$/;
            
            if(validacep.test(cep)) {
                $("#id_logradouro").val("...");
                $("#id_bairro").val("...");
                $("#id_cidade").val("...");
                $("#id_estado").val("...");
                $("#id_ibge").val("...");
                
                $.getJSON("https://viacep.com.br/ws/"+ cep +"/json/?callback=?", function(dados) {
                    if (!("erro" in dados)) {
                        $("#id_logradouro").val(dados.logradouro);
                        $("#id_bairro").val(dados.bairro);
                        $("#id_cidade").val(dados.localidade);
                        $("#id_estado").val(dados.uf);
                        $("#id_ibge").val(dados.ibge);
                    }
                    else {
                        limpa_formulário_cep();
                        alert("CEP não encontrado.");
                    }
                });
            }
            else {
                limpa_formulário_cep();
                alert("Formato de CEP inválido.");
            }
        }
        else {
            limpa_formulário_cep();
        }
    });
}); 