$(document).ready(function(){
    var $sistema = $("#id_sistema_operativo")
        $version = $("#id_version_sistema_op")
        $options = $version.find('option');
        $ofimatica = $("#id_ofimatica")
        $version_ofimatica = $("#id_version_ofimatica")
        $options_ofimatica = $version_ofimatica.find('option');


        $sistema.on("change", function(){
          $version.html($options.filter('[value="'+this.value+'"]'))
        }).trigger('change');

        $ofimatica.on("change", function(){
          $version_ofimatica.html($options_ofimatica.filter('[value="'+this.value+'"]'))
        }).trigger('change');
  });