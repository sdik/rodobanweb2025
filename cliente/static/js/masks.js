$(document).ready(function(){
    // Máscaras básicas
    $('.mask-cpf').mask('000.000.000-00');
    $('.mask-cnpj').mask('00.000.000/0000-00');
    $('.mask-cep').mask('00000-000');
    $('.mask-telefone').mask('(00) 0000-0000');
    $('.mask-celular').mask('(00) 00000-0000');
    
    // Máscara dinâmica para telefone/celular
    var SPMaskBehavior = function (val) {
        return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
    },
    spOptions = {
        onKeyPress: function(val, e, field, options) {
            field.mask(SPMaskBehavior.apply({}, arguments), options);
        }
    };
    
    $('.mask-telefone-dinamico').mask(SPMaskBehavior, spOptions);
}); 