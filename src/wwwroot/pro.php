<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Ma page de test</title>
    <script src="https://cdn.plot.ly/plotly-2.20.0.min.js"></script>
    <style>
      /*création des styles des boutons et des textes*/
      #candle {                               
        position: absolute;
        top: 673px;
        left: 371.5px;
        color: #8295b2;
        background: #1e1e1e;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: "Arial";
        font-weight: bold;
        width: 112.5px;
        height: 32px;
      }

      #minutes {
        position: absolute;
        top: 831px;
        left: 371.5px;
        color: #8295b2;
        background: #1e1e1e;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: "Arial";
        font-weight: bold;
        width: 112.5px;
        height: 32px;
      }

      #ema {
        position: absolute;
        top: 752px;
        left: 371.5px;
        color: #8295b2;
        background: #1e1e1e;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: "Arial";
        font-weight: bold;
        width: 112.5px;
        height: 32px;
      }

      #bollinger {
        position: absolute;
        top: 752px;
        left: 503px;
        color: #8295b2;
        background: #1e1e1e;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: "Arial";
        font-weight: bold;
        width: 112.5px;
        height: 32px;
      }

      #rsi {
        position: absolute;
        top: 752px;
        left: 634.5px;
        color: #8295b2;
        background: #1e1e1e;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: "Arial";
        font-weight: bold;
        width: 112.5px;
        height: 32px;
      }

      #macd {
        position: absolute;
        top: 752px;
        left: 766px;
        color: #8295b2;
        background: #1e1e1e;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: "Arial";
        font-weight: bold;
        width: 112.5px;
        height: 32px;
      }

      #so {
        position: absolute;
        top: 752px;
        left: 897.5px;
        color: #8295b2;
        background: #1e1e1e;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: "Arial";
        font-weight: bold;
        width: 112.5px;
        height: 32px;
      }

      #heurea {
        position: absolute;
        top: 673px;
        left: 644.5px;
        color: white;
        background: #546EE5;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: 'Arial';
        font-weight: bold;
        width: 68.67px;
        height: 32px;
      }

      #heureb {
        position: absolute;
        top: 673px;
        left: 732.17px;
        color: #8295B2;
        background: #1E1E1E;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: 'Arial';
        font-weight: bold;
        width: 68.67px;
        height: 32px;
      }

      #heurec {
        position: absolute;
        top: 673px;
        left: 819.84px;
        color: #8295B2;
        background: #1E1E1E;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: 'Arial';
        font-weight: bold;
        width: 68.67px;
        height: 32px;
      }

      #heured {
        position: absolute;
        top: 673px;
        left: 907.51px;
        color: #8295B2;
        background: #1E1E1E;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: 'Arial';
        font-weight: bold;
        width: 68.67px;
        height: 32px;
      }

      #forea {
        position: absolute;
        top: 831px;
        left: 644.5px;
        color: white;
        background: #546EE5;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: 'Arial';
        font-weight: bold;
        width: 68.67px;
        height: 32px;
      }

      #foreb {
        position: absolute;
        top: 831px;
        left: 732.17px;
        color: #8295B2;
        background: #1E1E1E;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: 'Arial';
        font-weight: bold;
        width: 68.67px;
        height: 32px;
      }

      #forec {
        position: absolute;
        top: 831px;
        left: 819.84px;
        color: #8295B2;
        background: #1E1E1E;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: 'Arial';
        font-weight: bold;
        width: 68.67px;
        height: 32px;
      }

      #fored {
        position: absolute;
        top: 831px;
        left: 907.51px;
        color: #8295B2;
        background: #1E1E1E;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: 'Arial';
        font-weight: bold;
        width: 68.67px;
        height: 32px;
      }

      #classic {
        position: absolute;
        top: 673px;
        left: 503px;
        color: white;
        background: #546ee5;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: "Arial";
        font-weight: bold;
        width: 112.5px;
        height: 32px;
      }

      #jours {
        position: absolute;
        top: 831px;
        left: 503px;
        color: white;
        background: #546ee5;
        border-radius: 40px;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;
        border: none;
        font-size: 12px;
        font-family: "Arial";
        font-weight: bold;
        width: 112.5px;
        height: 32px;
      }

      search {
        display: flex;
        flex-direction: row;
        align-items: center;
        padding: 0px 9px 0px 14px;
        position: absolute;
        width: 274px;
        height: 50px;
        left: 41px;
        top: 29px;
        background: #373d4c;
        border-radius: 22px;
      }

      .txt {
        font-family: "Arial";
        font-weight: bold;
        display: flex;
        align-items: center;
        color: #8295b2;
        font-size: 14px;
      }

      type {
        position: absolute;
        top: 649px;
        left: 371px;
      }

      mode {
        position: absolute;
        top: 807px;
        left: 371px;
      }

      outil {
        position: absolute;
        top: 728px;
        left: 371px;
      }

      heu {
        position: absolute;
        top: 649px;
        left: 644px;
      }

      fore {
        position: absolute;
        top: 807px;
        left: 644px;
      }

      .search-bar {
        background-color: #373d4c;
        border: none;
        padding: 10px;
        width: 50%;
        font-size: 16px;
      }

      .image-button {
        border: none;
        background-color: transparent;
        cursor: pointer;
        padding: 0;
      }

      .my-image {
        position: absolute;
        top: 42px;
        left: 290px;
        z-index: 2;
      }

      geom {
        position: absolute;
        left: 400px;
        top: 912px;
      }

      agentbased {
        position: absolute;
        left: 648px;
        top: 912px;
      }

      Prophet {
        position: absolute;
        left: 863px;
        top: 912px;
      }

      #sim1 {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;

        position: absolute;
        width: 102px;
        height: 32px;
        left: 862px;
        top: 961px;

        background: rgb(30, 30, 30);
        color: #8295B2;
        border-radius: 40px;
      }
      
      #sim2 {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;

        position: absolute;
        width: 102px;
        height: 32px;
        left: 640px;
        top: 961px;

        background: #373d4c;
        color: #8295b2;
        border-radius: 40px;
      }

      #sim3 {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
        padding: 9px;
        gap: 9px;

        position: absolute;
        width: 102px;
        height: 32px;
        left: 418px;
        top: 961px;

        background: rgb(30, 30, 30);
        color: #8295B2;
        border-radius: 40px;
      }

      #rec1 {
        box-sizing: border-box;
        position: absolute;
        width: 189px;
        height: 119px;
        left: 374px;
        top: 890px;
        border: 2px solid #222839;
        border-radius: 20px;
      }

      #rec2 {
        box-sizing: border-box;
        position: absolute;
        width: 189px;
        height: 119px;
        left: 596px;
        top: 890px;
        border: 2px solid #222839;
        border-radius: 20px;
      }

      #rec3 {
        box-sizing: border-box;
        position: absolute;
        width: 189px;
        height: 119px;
        left: 818px;
        top: 890px;
        border: 2px solid #222839;
        border-radius: 20px;
      }

      #rec4 {
        box-sizing: border-box;
        position: absolute;
        width: 302px;
        height: 300px;
        left: 35px;
        top: 620px;
        border: 2px solid #222839;
        border-radius: 20px;
        max-width: 370px; /* Limite de largeur */
        overflow: auto; /* Ajout de défilement en cas de dépassement */
      }
      .titre-statistiques {
        font-size: 14px;
        color: #8295B2;
        margin-bottom: 20px;
        margin-top: 20px;
        margin-left: auto;
        margin-right: auto;
        font-family: Arial, sans-serif;
        font-weight: bold;
        word-wrap: break-word;
        text-align: center;
      }

      ul {
        list-style-type: none;
        padding: 0;
      }

      li {
        margin-bottom: 10px;
      }

      .nom-statistique {
        color: #8295B2; 
        font-family: Arial, sans-serif; 
        font-size: 13px;
        margin-left: 50px;
      }

      .valeur-statistique {
        font-family: Arial, sans-serif; 
        font-size: 13px;
        color: white;
        word-wrap: break-word;
      }

      #rec5 {
        box-sizing: border-box;
        position: absolute;
        width: 302px;
        height: 300px;
<<<<<<< HEAD
        left : 1045px;
=======
        left: 1045px;
>>>>>>> 9c53553568637aa80faf4927cd388d5a0f99677a
        top: 620px;
        border: 2px solid #222839;
        border-radius: 20px;
        max-width: 370px; /* Limite de largeur */
        overflow: auto; /* Ajout de défilement en cas de dépassement */
      }
      .titre-infos-stock {
        position: absolute;
        font-family: Arial, sans-serif;
        font-size: 14px;
        color: #8295B2;
        word-wrap: break-word;
        text-align: center;
        margin-top: 20px;
        left: 50%;
        transform: translateX(-50%);
      }
      #nom-stock {
        position: relative;
        left: 50%;
        top: 70px;
        transform: translateX(-50%);
        font-family: Arial, sans-serif;
        color: white;
        font-size: 50px;
        text-align: center;
      }


      pageTitle .txt{
        position: absolute;
        top: 30px;
        left: 555px;
        font-size: 40px;
        color: #8295B2;
      }
    </style>
  </head>

  <body style="background-color: rgb(30, 30, 30)"> 
    <div id="tester" style="width: 1400px; height: 630px"></div>
    <div id="rec1"></div>
    <div id="rec2"></div>
    <div id="rec3"></div>
    <div id="rec4">
      <h2 class="titre-statistiques">OUTILS D'ANALYSE STATISTIQUES</h2>
      <ul id="liste-statistiques">
      </ul>
    </div>
    <div id="rec5">
      <h2 class="titre-infos-stock">SYMBOLE BOURSIER</h2>
      <p id="nom-stock"></p>
    </div>

    <type><span class="txt">Type</span></type>
    <mode><span class="txt">Mode</span></mode>
    <outil><span class="txt">Outils d'Analyse Technique</span></outil>
    <heu><span class="txt">Temps</span></heu>
    <fore><span class="txt">Forecasting</span></fore>
    <pageTitle><span class="txt">PRO3600 : Visualize Finance</span></pageTitle>

    <div style="text-align: center">
      <Prophet><span class="txt">Modèle<br />NeuralProphet</span></Prophet>
    </div>
    <div style="text-align: center">
      <geom><span class="txt">Modèle Géométrique<br />Brownien</span></geom>
    </div>
    <div style="text-align: center">
      <agentbased><span class="txt">Modèle Basé<br />Agent</span></agentbased>
    </div>

    <!-- Create the button -->
    <button id="candle">CANDLESTICKS</button>
    <button id="classic">CLASSIC</button>
    <button id="minutes">MINUTES</button>
    <button id="jours">JOURS</button>
    <button id="ema">EMA</button>
    <button id="bollinger">BOLLINGER</button>
    <button id="rsi">RSI</button>
    <button id="macd">MACD</button>
    <button id="so">SO</button>
    <button id="heurea">7J</button>
    <button id="heureb">1M</button>
    <button id="heurec">2M</button>
    <button id="heured">6M</button>
    <button id="forea">5J</button>
    <button id="foreb">15J</button>
    <button id="forec">1M</button>
    <button id="fored">2M</button>
    <button id="sim1">Simulation</button>
    <button id="sim2">Simulation</button>
    <button id="sim3">Simulation</button>


    <form method="POST" action="result">
        <search><input type="text" id="inputValue" name="inputValue" placeholder="Search..." class="search-bar"></search>
    </form>


    <?php
        $fabsi = file("./templates/absi.txt", FILE_IGNORE_NEW_LINES);
        $fordo = file("./templates/ordo.txt", FILE_IGNORE_NEW_LINES);
        $fopen = file("./templates/open.txt", FILE_IGNORE_NEW_LINES);
        $fclose = file("./templates/close.txt", FILE_IGNORE_NEW_LINES);
        $fhigh = file("./templates/high.txt", FILE_IGNORE_NEW_LINES);
        $flow = file("./templates/low.txt", FILE_IGNORE_NEW_LINES);
        $fewma = file("./templates/ewma.txt", FILE_IGNORE_NEW_LINES);
        $fbolup = file("./templates/bolup.txt", FILE_IGNORE_NEW_LINES);
        $fboldown = file("./templates/boldown.txt", FILE_IGNORE_NEW_LINES);
        $frsi = file("./templates/rsi.txt", FILE_IGNORE_NEW_LINES);
        $fmacd = file("./templates/macd.txt", FILE_IGNORE_NEW_LINES);
        $fsignal = file("./templates/signal.txt", FILE_IGNORE_NEW_LINES);
        $fhist = file("./templates/hist.txt", FILE_IGNORE_NEW_LINES);
        $frapidso = file("./templates/fastso.txt", FILE_IGNORE_NEW_LINES);
        $fslowso = file("./templates/slowso.txt", FILE_IGNORE_NEW_LINES);
        $frabsi = file("./templates/rabsi.txt", FILE_IGNORE_NEW_LINES);
        $fropen = file("./templates/ropen.txt", FILE_IGNORE_NEW_LINES);
        $frclose = file("./templates/rclose.txt", FILE_IGNORE_NEW_LINES);
        $frhigh = file("./templates/rhigh.txt", FILE_IGNORE_NEW_LINES);
        $frlow = file("./templates/rlow.txt", FILE_IGNORE_NEW_LINES);
        $frewma = file("./templates/rewma.txt", FILE_IGNORE_NEW_LINES);
        $frbolup = file("./templates/rbolup.txt", FILE_IGNORE_NEW_LINES);
        $frboldown = file("./templates/rboldown.txt", FILE_IGNORE_NEW_LINES);
        $frrsi = file("./templates/rrsi.txt", FILE_IGNORE_NEW_LINES);
        $frmacd = file("./templates/rmacd.txt", FILE_IGNORE_NEW_LINES);
        $frsignal = file("./templates/rsignal.txt", FILE_IGNORE_NEW_LINES);
        $frhist = file("./templates/rhist.txt", FILE_IGNORE_NEW_LINES);
        $frrapidso = file("./templates/rfastso.txt", FILE_IGNORE_NEW_LINES);
        $frslowso = file("./templates/rslowso.txt", FILE_IGNORE_NEW_LINES);
        $fbrownian = file("./templates/brownian.txt", FILE_IGNORE_NEW_LINES);
        $fabsi_pred = file("./templates/absi_pred.txt", FILE_IGNORE_NEW_LINES);
        $fneuralprophet = file("./templates/neuralprophet.txt", FILE_IGNORE_NEW_LINES);
        $fabsi_neural = file("./templates/absi_neural.txt", FILE_IGNORE_NEW_LINES);
        $fagent = file("./templates/PredictionAgent.txt", FILE_IGNORE_NEW_LINES);
        $fabsi_agent = file("./templates/PredictionHeure.txt", FILE_IGNORE_NEW_LINES);
        $fstats = file("./plot/stats.txt", FILE_IGNORE_NEW_LINES);
        $fstock_name = file("./templates/stock_name.txt", FILE_IGNORE_NEW_LINES);
    ?>
    <script>
        var candle = document.getElementById("candle");
        var classic = document.getElementById("classic");
        var jours = document.getElementById("jours");
        var minutes = document.getElementById("minutes");
        var ema = document.getElementById("ema");
        var bollinger = document.getElementById("bollinger");
        var rsi = document.getElementById("rsi");
        var macd = document.getElementById("macd");
        var so = document.getElementById("so");
        var heurea = document.getElementById("heurea");
        var heureb = document.getElementById("heureb");
        var heurec = document.getElementById("heurec");
        var heured = document.getElementById("heured");
        var forea = document.getElementById("forea");
        var foreb = document.getElementById("foreb");
        var forec = document.getElementById("forec");
        var fored = document.getElementById("fored");
        var sim1 = document.getElementById("sim1");
        var sim2 = document.getElementById("sim2");
        var sim3 = document.getElementById("sim3");

        var textheurea = document.getElementById("heurea");
        var textheureb = document.getElementById("heureb");
        var textheurec = document.getElementById("heurec");
        var textheured = document.getElementById("heured");
        var textforea = document.getElementById("forea");
        var textforeb = document.getElementById("foreb");
        var textforec = document.getElementById("forec");
        var textfored = document.getElementById("fored");


        var absi = JSON.parse('<?php echo json_encode($fabsi); ?>');
        var ordo = JSON.parse('<?php echo json_encode($fordo); ?>');
        var ope = JSON.parse('<?php echo json_encode($fopen); ?>');
        var close = JSON.parse('<?php echo json_encode($fclose); ?>');
        var high = JSON.parse('<?php echo json_encode($fhigh); ?>');
        var low = JSON.parse('<?php echo json_encode($flow); ?>');
        var ewma = JSON.parse('<?php echo json_encode($fewma); ?>');
        var bolup = JSON.parse('<?php echo json_encode($fbolup); ?>');
        var boldown = JSON.parse('<?php echo json_encode($fboldown); ?>');
        var rs = JSON.parse('<?php echo json_encode($frsi); ?>');
        var mac = JSON.parse('<?php echo json_encode($fmacd); ?>');
        var sig = JSON.parse('<?php echo json_encode($fsignal); ?>');
        var his = JSON.parse('<?php echo json_encode($fhist); ?>');
        var fasts = JSON.parse('<?php echo json_encode($frapidso); ?>');
        var slows = JSON.parse('<?php echo json_encode($fslowso); ?>');
        var rabsi = JSON.parse('<?php echo json_encode($frabsi); ?>');
        var rope = JSON.parse('<?php echo json_encode($fropen); ?>');
        var rclose = JSON.parse('<?php echo json_encode($frclose); ?>');
        var rhigh = JSON.parse('<?php echo json_encode($frhigh); ?>');
        var rlow = JSON.parse('<?php echo json_encode($frlow); ?>');
        var rewma = JSON.parse('<?php echo json_encode($frewma); ?>');
        var rbolup = JSON.parse('<?php echo json_encode($frbolup); ?>');
        var rboldown = JSON.parse('<?php echo json_encode($frboldown); ?>');
        var rrs = JSON.parse('<?php echo json_encode($frrsi); ?>');
        var rmac = JSON.parse('<?php echo json_encode($frmacd); ?>');
        var rsig = JSON.parse('<?php echo json_encode($frsignal); ?>');
        var rhis = JSON.parse('<?php echo json_encode($frhist); ?>');
        var rfasts = JSON.parse('<?php echo json_encode($frrapidso); ?>');
        var rslows = JSON.parse('<?php echo json_encode($frslowso); ?>');
        var brownian = JSON.parse('<?php echo json_encode($fbrownian); ?>');
        var absi_pred = JSON.parse('<?php echo json_encode($fabsi_pred); ?>');
        var neuralprophet = JSON.parse('<?php echo json_encode($fneuralprophet); ?>');
        var absi_neural = JSON.parse('<?php echo json_encode($fabsi_neural); ?>');
        var agent = JSON.parse('<?php echo json_encode($fagent); ?>');
        var absi_agent = JSON.parse('<?php echo json_encode($fabsi_agent); ?>');
        var stats = JSON.parse('<?php echo json_encode($fstats); ?>');
        var stock_name = JSON.parse('<?php echo json_encode($fstock_name); ?>');

        let intordo = ordo.map(parseFloat);
        let intopen = ope.map(parseFloat);
        let intclose = close.map(parseFloat);
        let inthigh = high.map(parseFloat);
        let intlow = low.map(parseFloat);
        let intewma = ewma.map(parseFloat);
        let intbolup = bolup.map(parseFloat);
        let intboldown = boldown.map(parseFloat);
        let intrsi = rs.map(parseFloat);
        let intmacd = mac.map(parseFloat);
        let intsignal = sig.map(parseFloat);
        let inthist = his.map(parseFloat);
        let intfastso = fasts.map(parseFloat);
        let intslowso = slows.map(parseFloat);
        let intbrownian = brownian.map(parseFloat);
        let intneuralprophet = neuralprophet.map(parseFloat);
        let intagent = agent.map(parseFloat);
        let intstats = stats.map(parseFloat);
        let dabsi = absi.map(function(dateString) {
          return new Date(dateString);
        });
        let dabsi_pred = absi_pred.map(function(dateString) {
          return new Date(dateString);
        });
        let intropen = rope.map(parseFloat);
        let intrclose = rclose.map(parseFloat);
        let intrhigh = rhigh.map(parseFloat);
        let intrlow = rlow.map(parseFloat);
        let intrewma = rewma.map(parseFloat);
        let intrbolup = rbolup.map(parseFloat);
        let intrboldown = rboldown.map(parseFloat);
        let intrrsi = rrs.map(parseFloat);
        let intrmacd = rmac.map(parseFloat);
        let intrsignal = rsig.map(parseFloat);
        let intrhist = rhis.map(parseFloat);
        let intrfastso = rfasts.map(parseFloat);
        let intrslowso = rslows.map(parseFloat);
        let drabsi = rabsi.map(function(dateString) {
          return new Date(dateString);
        });
        let dabsi_neural = absi_neural.map(function(dateString) {
          return new Date(dateString);
        });
        let dabsi_agent = absi_agent.map(function(dateString) {
          return new Date(dateString);
        });
        var cdl = false;
        var jr = true;
        var zm = 0;
        var fr = 0;
        var modele = 0;

        sim2.style.border = 'none';

        function chdate(x) {
          for (let i = 0; i < drabsi.length; i++) {
            if (x.getFullYear() === drabsi[i].getFullYear() && x.getMonth() === drabsi[i].getMonth() && x.getDate() === drabsi[i].getDate() && x.getHours() === drabsi[i].getHours() && x.getMinutes() === drabsi[i].getMinutes()) {
              return true;
            }
          }
          return false;
        }


        function cleaning() {
          let check = new Date(drabsi[0]);
          let rangebreaker = [];
          for (let i=1; i<drabsi.length; i++) {
            if (!(chdate(check))) {
              rangebreaker.push({bounds: [new Date(drabsi[i-2]), new Date(drabsi[i-1])]});
              check = new Date(drabsi[i]);
            }
            else {check.setMinutes(check.getMinutes()+1);}
          }
          rangebreaker.push({bounds: [new Date(drabsi[drabsi.length-1]), new Date(dabsi_agent[0])]});
          return rangebreaker;
        }

        function mynewFunction(y) {
          if (y==0) {x = 1;}
          else if (y==1) {x = 6;}
          else if (y==2) {x = 12;}
          else if (y==3) {x = 24;}
          window.filteredDates = drabsi.slice(-x*60-1, -1);
          window.subopen = intropen.slice(-filteredDates.length-1, -1);
          window.subclose = intrclose.slice(-filteredDates.length-1, -1);
          window.subhigh = intrhigh.slice(-filteredDates.length-1, -1);
          window.sublow = intrlow.slice(-filteredDates.length-1, -1);
          window.subordo = subclose;
          window.subewma = intrewma.slice(-filteredDates.length-1, -1);
          window.subbolup = intrbolup.slice(-filteredDates.length-1, -1);
          window.subboldown = intrboldown.slice(-filteredDates.length-1, -1);
          window.subrsi = intrrsi.slice(-filteredDates.length-1, -1);
          window.submacd = intrmacd.slice(-filteredDates.length-1, -1);
          window.subsignal = intrsignal.slice(-filteredDates.length-1, -1);
          window.subhist = intrhist.slice(-filteredDates.length-1, -1);
          window.subfastso = intrfastso.slice(-filteredDates.length-1, -1);
          window.subslowso = intrslowso.slice(-filteredDates.length-1, -1);
          window.layout = {
            paper_bgcolor:'rgba(0,0,0,0)',
            plot_bgcolor:'rgba(0,0,0,0)',
            xaxis: {
              rangebreaks: cleaning(),
              title: 'Time',
              titlefont: {
                color: 'rgb(220,220,220)' // Couleur de la police de l'axe X
              },
              tickfont: {
                color: 'rgb(220,220,220)' // Couleur de la police des graduations de l'axe X
              }
            },
            yaxis: {
            title: 'Price ($)',
            titlefont: {
              color: 'rgb(220,220,220)' // Couleur de la police de l'axe Y
            },
            tickfont: {
              color: 'rgb(220,220,220)' // Couleur de la police des graduations de l'axe Y
            }
            }
          };
        }

        function myFunctionD(y) {
          if (y==0) {x = 7;}
          else if (y==1) {x = 31;}
          else if (y==2) {x = 61;}
          else if (y==3) {x = 61*3;}
          const currentDate = new Date();
          let newdate = new Date();  // create a new date object
          newdate.setDate(currentDate.getDate() - x);  // take off x days to the date
          window.filteredDates = dabsi.filter(function(date) {
            let nDate = new Date(date);
            return (nDate >= newdate && nDate <= currentDate);
          });
          window.subordo = intordo.slice(-filteredDates.length-1, -1);
          window.subopen = intopen.slice(-filteredDates.length-1, -1);
          window.subclose = intclose.slice(-filteredDates.length-1, -1);
          window.subhigh = inthigh.slice(-filteredDates.length-1, -1);
          window.sublow = intlow.slice(-filteredDates.length-1, -1);
          window.subewma = intewma.slice(-filteredDates.length-1, -1);
          window.subbolup = intbolup.slice(-filteredDates.length-1, -1);
          window.subboldown = intboldown.slice(-filteredDates.length-1, -1);
          window.subrsi = intrsi.slice(-filteredDates.length-1, -1);
          window.submacd = intmacd.slice(-filteredDates.length-1, -1);
          window.subsignal = intsignal.slice(-filteredDates.length-1, -1);
          window.subhist = inthist.slice(-filteredDates.length-1, -1);
          window.subfastso = intfastso.slice(-filteredDates.length-1, -1);
          window.subslowso = intslowso.slice(-filteredDates.length-1, -1);
          window.layout = {
            paper_bgcolor:'rgba(0,0,0,0)',
            plot_bgcolor:'rgba(0,0,0,0)',
            xaxis: {
              title: 'Time',
              titlefont: {
                color: 'rgb(220,220,220)' // Couleur de la police de l'axe X
              },
              tickfont: {
                color: 'rgb(220,220,220)' // Couleur de la police des graduations de l'axe X
              }
            },
            yaxis: {
            title: 'Price ($)',
            titlefont: {
              color: 'rgb(220,220,220)' // Couleur de la police de l'axe Y
            },
            tickfont: {
              color: 'rgb(220,220,220)' // Couleur de la police des graduations de l'axe Y
            }
            }
          };
        }

        function filtragej(x,y) {
          const currentDate = new Date();
          let newdate1 = new Date();  // create a new date object
          let newdate2 = new Date();
          let newdate3 = new Date();
          if (x==0) {futur = 5; minu = 1;}
          else if (x==1) {futur = 15; minu = 2;}
          else if (x==2) {futur = 30; minu = 3;}
          else if (x==3) {futur = 61; minu = 6;}
          if (y==0) {passe = 7;}
          else if (y==1) {passe = 31;}
          else if (y==2) {passe = 61;}
          else if (y==3) {passe = 61*3;}
          newdate1.setDate(currentDate.getDate() + futur);  // add off x days to the date
          newdate2.setDate(currentDate.getDate() - passe);  // take off x days to the date
          window.filteredDates_pred = dabsi_pred.filter(function(date) {
            let nDate = new Date(date);
            return (nDate <= newdate1);
          });
          window.subbrownian = intbrownian.slice(0, filteredDates_pred.length);
          window.filteredDates_pred = filteredDates_pred.filter(function(date) {
            let nDate = new Date(date);
            return (nDate >= newdate2);
          });
          window.subbrownian = subbrownian.slice(-filteredDates_pred.length-1, -1);
          
          window.filteredDates_neural = dabsi_neural.filter(function(date) {
            let nDate = new Date(date);
            return (nDate <= newdate1);
          });
          window.subneuralprophet = intneuralprophet.slice(0, filteredDates_neural.length);
          window.filteredDates_neural = filteredDates_neural.filter(function(date) {
            let nDate = new Date(date);
            return (nDate >= newdate2);
          });
          window.subneuralprophet = subneuralprophet.slice(-filteredDates_neural.length-1, -1);

          newdate3.setMinutes(30);
          newdate3.setSeconds(0);
          newdate3.setMilliseconds(0);
          newdate3.setHours(13 + minu);

          window.filteredDates_agent = dabsi_agent.filter(function(date) {
            let nDate = new Date(date);
            return (nDate <= newdate3);
          });
          window.subagent = intagent.slice(0, filteredDates_agent.length);
        }

        myFunctionD(0);
        filtragej(0,0);
////////////////////////////////////////////////////////////////////////////
      
        function mycandle() {
            TESTER = document.getElementById('tester');
            Plotly.newPlot( TESTER, [{
            x: filteredDates,
            open: subopen,
            high: subhigh,
            close: subclose,
            low: sublow, type: 'candlestick'}], layout, {displayModeBar: false});
        }

        function myplot() {
          TESTER = document.getElementById('tester');
          Plotly.newPlot( TESTER, [{
          x: filteredDates,
          y: subordo,
          line: {color: 'rgb(52, 152, 219)'}
          }], layout, {displayModeBar: false});
        }

        function aiguille() {
          if (modele == 1) {
            mybrownian();
          }
          else if (modele == 2) {
            myagent();
          }
          else if (modele == 3) {
            myneural();
          }
          else if (modele == 4) {
            myewma();
          }
          else if (modele == 5) {
            mybollinger();
          }
          else if (modele == 6) {
            myrsi();
          }
          else if (modele == 7) {
            mymacd();
          }
          else if (modele == 8) {
            myso();
          }
          else if (modele == 0) {
          if (cdl) {
            mycandle();
          } else {myplot();}
        }
        }

        candle.addEventListener('click', function() {
          candle.style.backgroundColor ='#546EE5';
          candle.style.color = 'white';
          classic.style.backgroundColor ='rgb(30, 30, 30)';
          classic.style.color = '#8295B2';
          cdl = true;
          aiguille();
        });

        minutes.addEventListener('click', function() {
          if (modele == 1 || modele == 3) {modele = 0;}
          minutes.style.backgroundColor ='#546EE5';
          minutes.style.color = 'white';
          jours.style.backgroundColor ='rgb(30, 30, 30)';
          jours.style.color = '#8295B2';
          textheurea.textContent = "1H";
          textheureb.textContent = "6H";
          textheurec.textContent = "12H";
          textheured.textContent = "1J";
          textforea.textContent = "1H";
          textforeb.textContent = "2H";
          textforec.textContent = "3H";
          textfored.textContent = "6H";
          if (jr) {
            sim2.style.border = sim1.style.borderStyle;
            sim3.style.border = 'none';
            sim1.style.border = 'none';
            sim2.style.backgroundColor ='rgb(30, 30, 30)';
            sim2.style.color = '#8295B2';
            sim3.style.backgroundColor ='#373d4c';
            sim3.style.color = '#8295B2';
            sim1.style.backgroundColor ='#373d4c';
            sim1.style.color = '#8295B2';}
          jr = false;
          mynewFunction(zm);
          aiguille();
        });

        classic.addEventListener('click', function() {
          classic.style.backgroundColor ='#546EE5'
          classic.style.color = 'white';
          candle.style.backgroundColor ='rgb(30, 30, 30)';
          candle.style.color = '#8295B2';
          cdl = false;
          aiguille();
        });

        jours.addEventListener('click', function() {
          if (modele == 2) {modele = 0;}
          jours.style.backgroundColor ='#546EE5'
          jours.style.color = 'white';
          minutes.style.backgroundColor ='rgb(30, 30, 30)';
          minutes.style.color = '#8295B2';
          textheurea.textContent = "7J";
          textheureb.textContent = "1M";
          textheurec.textContent = "2M";
          textheured.textContent = "6M";
          textforea.textContent = "5J";
          textforeb.textContent = "15J";
          textforec.textContent = "1M";
          textfored.textContent = "2M";
          if (!jr) {
            sim3.style.border = sim2.style.borderStyle;
            sim1.style.border = sim2.style.borderStyle;
            sim2.style.border = 'none';
            sim2.style.backgroundColor ='#373d4c';
            sim2.style.color = '#8295B2';
            sim3.style.backgroundColor ='rgb(30, 30, 30)';
            sim3.style.color = '#8295B2';
            sim1.style.backgroundColor ='rgb(30, 30, 30)';
            sim1.style.color = '#8295B2';}
          jr = true
          myFunctionD(zm);
          aiguille();
        });

        heurea.addEventListener('click', function() {
          zm = 0;
          heurea.style.backgroundColor ='#546EE5'
          heurea.style.color = 'white';
          heureb.style.backgroundColor ='rgb(30, 30, 30)';
          heureb.style.color = '#8295B2';
          heurec.style.backgroundColor ='rgb(30, 30, 30)';
          heurec.style.color = '#8295B2';
          heured.style.backgroundColor ='rgb(30, 30, 30)';
          heured.style.color = '#8295B2';
          if (jr) {myFunctionD(zm);}
          else {mynewFunction(zm);}
          filtragej(fr,zm);
          aiguille();
        });

        heureb.addEventListener('click', function() {
          zm = 1;
          heureb.style.backgroundColor ='#546EE5'
          heureb.style.color = 'white';
          heurea.style.backgroundColor ='rgb(30, 30, 30)';
          heurea.style.color = '#8295B2';
          heurec.style.backgroundColor ='rgb(30, 30, 30)';
          heurec.style.color = '#8295B2';
          heured.style.backgroundColor ='rgb(30, 30, 30)';
          heured.style.color = '#8295B2';
          if (jr) {myFunctionD(zm);}
          else {mynewFunction(zm);}
          filtragej(fr,zm);
          aiguille();
        });

        heurec.addEventListener('click', function() {
          zm = 2;
          heurec.style.backgroundColor ='#546EE5'
          heurec.style.color = 'white';
          heureb.style.backgroundColor ='rgb(30, 30, 30)';
          heureb.style.color = '#8295B2';
          heurea.style.backgroundColor ='rgb(30, 30, 30)';
          heurea.style.color = '#8295B2';
          heured.style.backgroundColor ='rgb(30, 30, 30)';
          heured.style.color = '#8295B2';
          if (jr) {myFunctionD(zm);}
          else {mynewFunction(zm);}
          filtragej(fr,zm);
          aiguille();
        });

        heured.addEventListener('click', function() {
          zm = 3;
          heured.style.backgroundColor ='#546EE5'
          heured.style.color = 'white';
          heureb.style.backgroundColor ='rgb(30, 30, 30)';
          heureb.style.color = '#8295B2';
          heurec.style.backgroundColor ='rgb(30, 30, 30)';
          heurec.style.color = '#8295B2';
          heurea.style.backgroundColor ='rgb(30, 30, 30)';
          heurea.style.color = '#8295B2';
          if (jr) {myFunctionD(zm);}
          else {mynewFunction(zm);}
          filtragej(fr,zm);
          aiguille();
        });

        forea.addEventListener('click', function() {
          fr = 0;
          forea.style.backgroundColor ='#546EE5'
          forea.style.color = 'white';
          foreb.style.backgroundColor ='rgb(30, 30, 30)';
          foreb.style.color = '#8295B2';
          forec.style.backgroundColor ='rgb(30, 30, 30)';
          forec.style.color = '#8295B2';
          fored.style.backgroundColor ='rgb(30, 30, 30)';
          fored.style.color = '#8295B2';
          filtragej(fr,zm);
          if (modele == 1) {
            mybrownian();
          }
          else if (modele == 2) {
            myagent();
          }
          else if (modele == 3) {
            myneural();
          }
          else if (modele == 0) {
          if (cdl) {
            mycandle();
          } else {myplot();}
        }});

        foreb.addEventListener('click', function() {
          fr = 1;
          foreb.style.backgroundColor ='#546EE5'
          foreb.style.color = 'white';
          forea.style.backgroundColor ='rgb(30, 30, 30)';
          forea.style.color = '#8295B2';
          forec.style.backgroundColor ='rgb(30, 30, 30)';
          forec.style.color = '#8295B2';
          fored.style.backgroundColor ='rgb(30, 30, 30)';
          fored.style.color = '#8295B2';
          filtragej(fr,zm);
          if (modele == 1) {
            mybrownian();
          }
          else if (modele == 2) {
            myagent();
          }
          else if (modele == 3) {
            myneural();
          }
          else if (modele == 0) {
          if (cdl) {
            mycandle();
          } else {myplot();}
        }
        });

        forec.addEventListener('click', function() {
          fr = 2;
          forec.style.backgroundColor ='#546EE5'
          forec.style.color = 'white';
          foreb.style.backgroundColor ='rgb(30, 30, 30)';
          foreb.style.color = '#8295B2';
          forea.style.backgroundColor ='rgb(30, 30, 30)';
          forea.style.color = '#8295B2';
          fored.style.backgroundColor ='rgb(30, 30, 30)';
          fored.style.color = '#8295B2';
          filtragej(fr,zm);
          if (modele == 1) {
            mybrownian();
          }
          else if (modele == 2) {
            myagent();
          }
          else if (modele == 3) {
            myneural();
          }
          else if (modele == 0) {
          if (cdl) {
            mycandle();
          } else {myplot();}
        }
        });

        fored.addEventListener('click', function() {
          fr = 3;
          fored.style.backgroundColor ='#546EE5'
          fored.style.color = 'white';
          foreb.style.backgroundColor ='rgb(30, 30, 30)';
          foreb.style.color = '#8295B2';
          forec.style.backgroundColor ='rgb(30, 30, 30)';
          forec.style.color = '#8295B2';
          forea.style.backgroundColor ='rgb(30, 30, 30)';
          forea.style.color = '#8295B2';
          filtragej(fr,zm);
          if (modele == 1) {
            mybrownian();
          }
          else if (modele == 2) {
            myagent();
          }
          else if (modele == 3) {
            myneural();
          }
          else if (modele == 0) {
          if (cdl) {
            mycandle();
          } else {myplot();}
        }
        });

     //////////////////////////////////////////////////////////////////////////
     function myewma() {
          if (cdl) {
            TESTER = document.getElementById('tester');
            Plotly.newPlot( TESTER, [{
            x: filteredDates,
            y: subewma,
            name: 'SMA',
            line: {color: 'rgb(243, 156, 18)'}
            },{
            x: filteredDates,
            open: subopen,
            high: subhigh,
            close: subclose,
            low: sublow, type: 'candlestick'}], layout, {displayModeBar: false});
          } else {
            TESTER = document.getElementById('tester');
            Plotly.newPlot( TESTER, [{
            x: filteredDates,
            y: subewma,
            name: 'SMA',
            line: {color: 'rgb(243, 156, 18)'}
            },{
            x: filteredDates,
            y: subordo,
            name: 'Stock Price',
            line: {color: 'rgb(52, 152, 219)'}
            }], layout, {displayModeBar: false});
          }
        }

        ema.addEventListener('click', function() {
          if (ema.style.backgroundColor == 'rgb(30, 30, 30)') {
            modele = 4;
            ema.style.backgroundColor ='#546EE5'
            ema.style.color = 'white';
            bollinger.style.backgroundColor ='rgb(30, 30, 30)';
            bollinger.style.color = '#8295B2';
            macd.style.backgroundColor ='rgb(30, 30, 30)';
            macd.style.color = '#8295B2';
            rsi.style.backgroundColor ='rgb(30, 30, 30)';
            rsi.style.color = '#8295B2';
            so.style.backgroundColor ='rgb(30, 30, 30)';
            so.style.color = '#8295B2';
            if (jr) {
            sim3.style.backgroundColor ='rgb(30, 30, 30)';
            sim3.style.color = '#8295B2';
            sim1.style.backgroundColor ='rgb(30, 30, 30)';
            sim1.style.color = '#8295B2';}
          else {
            sim2.style.backgroundColor ='rgb(30, 30, 30)';
            sim2.style.color = '#8295B2';
          }
            myewma();
          } else {
            ema.style.backgroundColor ='rgb(30, 30, 30)';
            ema.style.color = '#8295B2';
            modele = 0;
            if (cdl) {
              mycandle();
            } else {myplot();}
          }
        });
/////////////////////////////////////////////////////////////////////////////////

        function mybollinger() {
            if (cdl) {
                TESTER = document.getElementById('tester');
                Plotly.newPlot( TESTER, [{
                x: filteredDates,
                y: subbolup,
                name: 'Bollinger Up',
                line: {color:'rgb(52, 213, 69)'}
                },{
                x: filteredDates,
                y: subboldown,
                name: 'Bollinger Down',
                line: {color:'rgb(243, 58, 18)'}
                },{
                x: filteredDates,
                open: subopen,
                high: subhigh,
                close: subclose,
                low: sublow, type: 'candlestick'}], layout);
            } else {
                TESTER = document.getElementById('tester');
                Plotly.newPlot( TESTER, [{
                x: filteredDates,
                y: subbolup,
                name: 'Bollinger Up',
                line: {color:'rgb(52, 213, 69)'}
                },{
                x: filteredDates,
                y: subboldown,
                name: 'Bollinger Down',
                line: {color:'rgb(243, 58, 18)'}
                },{
                x: filteredDates,
                y: subordo,
                name: 'Stock Price',
                line: {color: 'rgb(52, 152, 219)'}}], layout);
            }
        } 

        bollinger.addEventListener('click', function() {
            if (bollinger.style.backgroundColor == 'rgb(30, 30, 30)') {
                modele = 5;
                bollinger.style.backgroundColor ='#546EE5'
                bollinger.style.color = 'white';
                ema.style.backgroundColor ='rgb(30, 30, 30)';
                ema.style.color = '#8295B2';
                macd.style.backgroundColor ='rgb(30, 30, 30)';
                macd.style.color = '#8295B2';
                rsi.style.backgroundColor ='rgb(30, 30, 30)';
                rsi.style.color = '#8295B2';
                so.style.backgroundColor ='rgb(30, 30, 30)';
                so.style.color = '#8295B2';
                if (jr) {
            sim3.style.backgroundColor ='rgb(30, 30, 30)';
            sim3.style.color = '#8295B2';
            sim1.style.backgroundColor ='rgb(30, 30, 30)';
            sim1.style.color = '#8295B2';}
          else {
            sim2.style.backgroundColor ='rgb(30, 30, 30)';
            sim2.style.color = '#8295B2';
          }
                mybollinger();
            } else {
                bollinger.style.backgroundColor ='rgb(30, 30, 30)';
                bollinger.style.color = '#8295B2';
                modele = 0;
                if (cdl) {
                mycandle();
                } else {myplot();}
            }
        });
/////////////////////////////////////////////////////////////////////////////////////
        function myrsi() {
          if (cdl) {
            TESTER = document.getElementById('tester');
            Plotly.newPlot( TESTER, [{
            x: filteredDates,
            y: subrsi,
            name: 'RSI',
            line: {color: 'rgb(243, 156, 18)'}
            },
            {
            x: filteredDates,
            open: subopen,
            high: subhigh,
            close: subclose,
            low: sublow, type: 'candlestick'}], layout, {displayModeBar: false});
          } else {
            TESTER = document.getElementById('tester');
            Plotly.newPlot( TESTER, [{
            x: filteredDates,
            y: subrsi,
            name: 'RSI',
            line: {color: 'rgb(243, 156, 18)'}
            },{
            x: filteredDates,
            y: subordo,
            name: 'Stock Price',
            line: {color: 'rgb(52, 152, 219)'} }], layout, {displayModeBar: false});
          }
        }

        rsi.addEventListener('click', function() {
          if (rsi.style.backgroundColor == 'rgb(30, 30, 30)') {
            modele = 6;
            rsi.style.backgroundColor ='#546EE5'
            rsi.style.color = 'white';
            bollinger.style.backgroundColor ='rgb(30, 30, 30)';
            bollinger.style.color = '#8295B2';
            macd.style.backgroundColor ='rgb(30, 30, 30)';
            macd.style.color = '#8295B2';
            ema.style.backgroundColor ='rgb(30, 30, 30)';
            ema.style.color = '#8295B2';
            so.style.backgroundColor ='rgb(30, 30, 30)';
            so.style.color = '#8295B2';
            if (jr) {
            sim3.style.backgroundColor ='rgb(30, 30, 30)';
            sim3.style.color = '#8295B2';
            sim1.style.backgroundColor ='rgb(30, 30, 30)';
            sim1.style.color = '#8295B2';}
          else {
            sim2.style.backgroundColor ='rgb(30, 30, 30)';
            sim2.style.color = '#8295B2';
          }
            myrsi();
          } else {
            modele = 0;
            rsi.style.backgroundColor ='rgb(30, 30, 30)';
            rsi.style.color = '#8295B2';
            if (cdl) {
              mycandle();
            } else {myplot();
            }
          }
        });
/////////////////////////////////////////////////////////////////////////
    function mymacd() {
          if (cdl) {
            TESTER = document.getElementById('tester');
            Plotly.newPlot( TESTER, [{
            x: filteredDates,
            y: submacd,
            name: 'MACD'
            },{
            x: filteredDates,
            y: subsignal,
            name: 'Signal'
            },{
              x: filteredDates,
              y: subhist,
              name: 'Difference',
              type:'bar'
            }], layout, {displayModeBar: false});
          } else {
            TESTER = document.getElementById('tester');
            Plotly.newPlot( TESTER, [{
            x: filteredDates,
            y: submacd,
            name: 'MACD',
            },{
            x: filteredDates,
            y: subsignal, 
            name: 'Signal'
            },{
            x: filteredDates,
            y: subhist,
            name: 'Difference',
            type:'bar'}], layout,{displayModeBar: false});
          }
        }


        macd.addEventListener('click', function() {
          if (macd.style.backgroundColor == 'rgb(30, 30, 30)') {
            modele = 7;
            macd.style.backgroundColor ='#546EE5'
            macd.style.color = 'white';
            bollinger.style.backgroundColor ='rgb(30, 30, 30)';
            bollinger.style.color = '#8295B2';
            ema.style.backgroundColor ='rgb(30, 30, 30)';
            ema.style.color = '#8295B2';
            rsi.style.backgroundColor ='rgb(30, 30, 30)';
            rsi.style.color = '#8295B2';
            so.style.backgroundColor ='rgb(30, 30, 30)';
            so.style.color = '#8295B2';
            if (jr) {
            sim3.style.backgroundColor ='rgb(30, 30, 30)';
            sim3.style.color = '#8295B2';
            sim1.style.backgroundColor ='rgb(30, 30, 30)';
            sim1.style.color = '#8295B2';}
          else {
            sim2.style.backgroundColor ='rgb(30, 30, 30)';
            sim2.style.color = '#8295B2';
          }
            mymacd();
          } else {
            modele = 0;
            macd.style.backgroundColor ='rgb(30, 30, 30)';
            macd.style.color = '#8295B2';
            if (cdl) {
              mycandle();
            } else {myplot();
            }
          }
        });

/////////////////////////////////////////////////////////////////////////////
        const list_20 = [];
        const list_80 = [];

          for (let i = 0; i < 2000; i++) {
            list_20.push(20);
            list_80.push(80);
          }

          function myso() {
          if (cdl) {
            TESTER = document.getElementById('tester');
            Plotly.newPlot( TESTER, [{
            x: filteredDates,
            y: subfastso,
            line:{
              color: 'rgb(142, 68, 173)'
            },
            name: 'Fast Stochastic Oscillator'
            },{
            x: filteredDates,
            y: subslowso,
            name: 'Slow Stochastic Oscillator'
            },{
            x: filteredDates,
            y: list_20,
            name: 'Oversold',
            mode: 'lines',
            line: {
              dash: 'dot',
              color: 'rgb(52, 213, 69)',
              width: 4
            }
            },{
            x: filteredDates,
            y: list_80,
            mode: 'lines',
            name: 'Overbought',
            line: {
              dash: 'dot',
              color: 'rgb(243, 58, 18)',
              width: 4
            }
            }], layout, {displayModeBar: false});
          } else {
            TESTER = document.getElementById('tester');
            Plotly.newPlot( TESTER, [{
            x: filteredDates,
            y: subfastso,
            name: 'Fast Stochastic Oscillator',
            line:{
              color: 'rgb(142, 68, 173)'
            }
            },{
            x: filteredDates,
            y: subslowso,
            name: 'Slow Stochastic Oscillator'
            },{
            x: filteredDates,
            y: list_20,
            name: 'Oversold',
            mode: 'lines',
            line: {
              dash: 'dot',
              color: 'rgb(52, 213, 69)',
              width: 4
            }
            },{
            x: filteredDates,
            y: list_80,
            mode: 'lines',
            name: 'Overbought',
            line: {
              dash: 'dot',
              color: 'rgb(243, 58, 18)',
              width: 4
            }
            }], layout, {displayModeBar: false});
          }
        }

        so.addEventListener('click', function() {
          if (so.style.backgroundColor == 'rgb(30, 30, 30)') {
            modele = 8;
            so.style.backgroundColor ='#546EE5'
            so.style.color = 'white';
            bollinger.style.backgroundColor ='rgb(30, 30, 30)';
            bollinger.style.color = '#8295B2';
            macd.style.backgroundColor ='rgb(30, 30, 30)';
            macd.style.color = '#8295B2';
            rsi.style.backgroundColor ='rgb(30, 30, 30)';
            rsi.style.color = '#8295B2';
            ema.style.backgroundColor ='rgb(30, 30, 30)';
            ema.style.color = '#8295B2';
            if (jr) {
            sim3.style.backgroundColor ='rgb(30, 30, 30)';
            sim3.style.color = '#8295B2';
            sim1.style.backgroundColor ='rgb(30, 30, 30)';
            sim1.style.color = '#8295B2';}
          else {
            sim2.style.backgroundColor ='rgb(30, 30, 30)';
            sim2.style.color = '#8295B2';
          }
            myso();
          } else {
            modele = 0;
            so.style.backgroundColor ='rgb(30, 30, 30)';
            so.style.color = '#8295B2';
            if (cdl) {
              mycandle();
            } else {myplot();
            }
          }
        });
////////////////////////////////////////////////////////////////:
        function mybrownian() {
          TESTER = document.getElementById('tester');
          if (cdl) {
            Plotly.newPlot( TESTER, [{
            x: filteredDates_pred,
            y: subbrownian,
            name: 'Brownian',
            line: {color: 'rgb(243, 156, 18)'}
            },{
            x: filteredDates,
            open: subopen,
            high: subhigh,
            close: subclose,
            low: sublow, 
            type: 'candlestick',
            name: 'Stock Price',
            line: {color: 'rgb(52, 152, 219)'}
            }], layout, {displayModeBar: false});
          }
          else {
            Plotly.newPlot( TESTER, [{
            x: filteredDates_pred,
            y: subbrownian,
            name: 'Brownian',
            line: {color: 'rgb(243, 156, 18)'}
            },{
            x: filteredDates,
            y: subordo,
            name: 'Stock Price',
            line: {color: 'rgb(52, 152, 219)'}
            }], layout, {displayModeBar: false});
          }
        }

        sim3.addEventListener('click', function() {
          if (jr) {
          if (sim3.style.backgroundColor == 'rgb(30, 30, 30)') {
            sim3.style.backgroundColor ='#546EE5'
            sim3.style.color = 'white';
            bollinger.style.backgroundColor ='rgb(30, 30, 30)';
            bollinger.style.color = '#8295B2';
            macd.style.backgroundColor ='rgb(30, 30, 30)';
            macd.style.color = '#8295B2';
            rsi.style.backgroundColor ='rgb(30, 30, 30)';
            rsi.style.color = '#8295B2';
            so.style.backgroundColor ='rgb(30, 30, 30)';
            so.style.color = '#8295B2';
            ema.style.backgroundColor ='rgb(30, 30, 30)';
            ema.style.color = '#8295B2';
            modele = 1;
            sim1.style.backgroundColor ='rgb(30, 30, 30)';
            sim1.style.color = '#8295B2';
            mybrownian();
          } else {
            sim3.style.backgroundColor ='rgb(30, 30, 30)';
            sim3.style.color = '#8295B2';
            modele = 0;
            if (cdl) {
              mycandle();
            } else {
              myplot();
            }
          }}
        });

        ////////////////////////////////////////////////////////////////:
        function myagent() {
          TESTER = document.getElementById('tester');
          if (cdl) {
            Plotly.newPlot( TESTER, [{
            x: filteredDates_agent,
            y: subagent,
            name: 'Agent',
            line: {color: 'rgb(243, 156, 18)'}
            },{
            x: filteredDates,
            open: subopen,
            high: subhigh,
            close: subclose,
            low: sublow, 
            type: 'candlestick',
            name: 'Stock Price',
            line: {color: 'rgb(52, 152, 219)'}
            }], layout, {displayModeBar: false});
          }
          else {
            Plotly.newPlot( TESTER, [{
            x: filteredDates_agent,
            y: subagent,
            name: 'Agent',
            line: {color: 'rgb(243, 156, 18)'}
            },{
            x: filteredDates,
            y: subordo,
            name: 'Stock Price',
            line: {color: 'rgb(52, 152, 219)'}
            }], layout, {displayModeBar: false});
          }
        }

        sim2.addEventListener('click', function() {
          if (!jr) {
          if (sim2.style.backgroundColor == 'rgb(30, 30, 30)') {
            sim2.style.backgroundColor ='#546EE5'
            sim2.style.color = 'white';
            bollinger.style.backgroundColor ='rgb(30, 30, 30)';
            bollinger.style.color = '#8295B2';
            macd.style.backgroundColor ='rgb(30, 30, 30)';
            macd.style.color = '#8295B2';
            rsi.style.backgroundColor ='rgb(30, 30, 30)';
            rsi.style.color = '#8295B2';
            so.style.backgroundColor ='rgb(30, 30, 30)';
            so.style.color = '#8295B2';
            ema.style.backgroundColor ='rgb(30, 30, 30)';
            ema.style.color = '#8295B2';
            modele = 2;
            myagent();
          } else {
            sim2.style.backgroundColor ='rgb(30, 30, 30)';
            sim2.style.color = '#8295B2';
            modele = 0;
            if (cdl) {
              mycandle();
            } else {
              myplot();
            }
          }}
        });

        ///////////////////////////////////////////////////////////
        function myneural() {
            TESTER = document.getElementById('tester');
            if (cdl) {
              Plotly.newPlot( TESTER, [{
              x: filteredDates_neural,
              y: subneuralprophet,
              name: 'Neural',
              line: {color: 'rgb(243, 156, 18)'}
              },{
              x: filteredDates,
              open: subopen,
              high: subhigh,
              close: subclose,
              low: sublow, 
              type: 'candlestick',
              name: 'Stock Price',
              line: {color: 'rgb(52, 152, 219)'}
              }], layout, {displayModeBar: false});
            }
            else {
              Plotly.newPlot( TESTER, [{
              x: filteredDates_neural,
              y: subneuralprophet,
              name: 'Neural',
              line: {color: 'rgb(243, 156, 18)'}
              },{
              x: filteredDates,
              y: subordo,
              name: 'Stock Price',
              line: {color: 'rgb(52, 152, 219)'}
              }], layout, {displayModeBar: false});
          }
        }

        sim1.addEventListener('click', function() {
          if (jr) {
          if (sim1.style.backgroundColor == 'rgb(30, 30, 30)') {
            sim1.style.backgroundColor ='#546EE5'
            sim1.style.color = 'white';
            bollinger.style.backgroundColor ='rgb(30, 30, 30)';
            bollinger.style.color = '#8295B2';
            macd.style.backgroundColor ='rgb(30, 30, 30)';
            macd.style.color = '#8295B2';
            rsi.style.backgroundColor ='rgb(30, 30, 30)';
            rsi.style.color = '#8295B2';
            so.style.backgroundColor ='rgb(30, 30, 30)';
            so.style.color = '#8295B2';
            ema.style.backgroundColor ='rgb(30, 30, 30)';
            ema.style.color = '#8295B2';
            modele = 3;
            sim3.style.backgroundColor ='rgb(30, 30, 30)';
            sim3.style.color = '#8295B2';
            myneural();
          } else {
            sim1.style.backgroundColor ='rgb(30, 30, 30)'
            sim1.style.color = '#8295B2';
            modele = 0;
            if (cdl) {
              mycandle();
            } else {
              myplot();
            }
          }}
        });

      myplot();

    </script>

    <script>
      // Liste des valeurs des statistiques, 3 chiffres après la virgule
      var valeurs = intstats;
      var valeursStatistiques = valeurs.map(function(nombre) {
        return nombre.toFixed(3);
      });
      var nomsStatistiques = ["Avg Log Return","Avg Absolute Yield","Standart Deviation","Kurtosis","Skewness","Studentized Range","Rank Correlation 1","Rank Corrolation 10"];

      // Sélection de l'élément <ul> qui contiendra les statistiques
      var listeStatistiques = document.getElementById('liste-statistiques');

      // Parcourir la liste des valeurs et générer les statistiques
      for (var i = 0; i < valeursStatistiques.length; i++) {
        // Crée un nouvel élément <li>
        var nouvelElementLi = document.createElement('li');

        // Crée un élément <strong> pour le nom de la statistique
        var nouvelElementNomStatistique = document.createElement('strong');
        nouvelElementNomStatistique.className = 'nom-statistique';
        nouvelElementNomStatistique.textContent = nomsStatistiques[i] + " : "

        // Crée un élément <span> pour la valeur de la statistique
        var nouvelElementValeurStatistique = document.createElement('span');
        nouvelElementValeurStatistique.className = 'valeur-statistique';
        nouvelElementValeurStatistique.textContent = valeursStatistiques[i];

        // Ajouter les éléments au <li>
        nouvelElementLi.appendChild(nouvelElementNomStatistique);
        nouvelElementLi.appendChild(nouvelElementValeurStatistique);

        // Ajouter le <li> à la liste des statistiques
        listeStatistiques.appendChild(nouvelElementLi);
      }
    </script>
    <script>

      // Sélectionnez l'élément <p> avec l'ID "nom-stock"
      var elementNomStock = document.getElementById("nom-stock");

      // Attribuez la valeur de la variable "stock_name" à l'élément <p>
      elementNomStock.textContent = stock_name;
    </script>
  </body>
</html>
