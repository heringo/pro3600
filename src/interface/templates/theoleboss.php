<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Ma page de test</title>
    <script src="https://cdn.plot.ly/plotly-2.20.0.min.js"></script>
    <style>
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

      #sevenDay{
        position: absolute;
        top: 673px;
        left: 818px;
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
      #thirtyDay {
        position: absolute;
        top: 673px;
        left: 890px;
        color: white;
        background: #546ee5;
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
      #sixtyDay {
        position: absolute;
        top: 673px;
        left: 960px;
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

      #heurea {
        position: absolute;
        top: 673px;
        left: 644.5px;
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
        left: 391px;
        top: 822px;
      }

      agentbased {
        position: absolute;
        left: 636px;
        top: 822px;
      }

      Prophet {
        position: absolute;
        left: 835px;
        top: 827px;
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

        background: #373d4c;
        color: #8295b2;
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
        left: 414px;
        top: 961px;

        background: #373d4c;
        color: #8295b2;
        border-radius: 40px;
      }
      #rec1 {
        box-sizing: border-box;
        position: absolute;
        width: 189px;
        height: 209px;
        left: 374px;
        top: 800px;
        border: 1px solid #222839;
        border-radius: 20px;
      }
      #rec2 {
        box-sizing: border-box;
        position: absolute;
        width: 189px;
        height: 209px;
        left: 596px;
        top: 799px;
        border: 1px solid #222839;
        border-radius: 20px;
      }
      #rec3 {
        box-sizing: border-box;
        position: absolute;
        width: 189px;
        height: 209px;
        left: 818px;
        top: 799px;
        border: 1px solid #222839;
        border-radius: 20px;
      }
      #rec4 {
        box-sizing: border-box;
        position: absolute;
        width: 302px;
        height: 361px;
        left: 41px;
        top: 648px;
        border: 1px solid #222839;
        border-radius: 20px;
      }
      #rec5 {
        box-sizing: border-box;
        position: absolute;
        width: 370px;
        height: 887px;
        left: 1062px;
        top: 99px;
        border: 1px solid #222839;
        border-radius: 20px;
      }
      #rec6 {
        display: flex;
        justify-content: center;
        lign-items: center;
        box-sizing: border-box;
        position: absolute;
        width: 220px;
        height: 54px;
        left: 814px;
        top: 665px;
        border: 1px solid #222839;
        border-radius: 20px;
      }
      #rec7 {
        display: flex;
        justify-content: center;
        align-items: center;
        box-sizing: border-box;
        position: absolute;
        width: 165px;
        height: 54px;
        left: 640px;
        top: 665px;
        border: 1px solid #222839;
        border-radius: 20px;
      }
      #rec8 {
        display: flex;
        justify-content: center;
        align-items: center;
        box-sizing: border-box;
        position: absolute;
        width: 253px;
        height: 54px;
        left: 367px;
        top: 665px;
        border: 1px solid #222839;
        border-radius: 20px;
      }
      OAS {
        position: absolute;
        left: 77px;
        top: 659px;
      }
      lastPrice {
        position: absolute;
        top: 22px;
        left: 545px;
      }
      hourChange {
        position: absolute;
        top: 22px;
        left: 665.5px;
      }
      hourHigh {
        position: absolute;
        top: 22px;
        left: 805px;
      }
      hourLow {
        position: absolute;
        top: 22px;
        left: 929.5px;
      }
      hourVolume {
        position: absolute;
        top: 22px;
        left: 1050px;
      }
      actualPrice {
        position: absolute;
        left: 1166px;
        top: 29px;
      }
      sellHistoric {
        position: absolute;
        top: 114.2px;
        left: 1076px;
      }
      buyHistoric {
        position: absolute;
        top: 564.2px;
        left: 1076px;
      }
      Price {
        position: absolute;
        top: 154px;
        left: 1076px;
      }
      Amount {
        position: absolute;
        top: 154px;
        left: 1182px;
      }
      Total {
        position: absolute;
        top: 154px;
        left: 1296px;
      }
    </style>
  </head>

  <body style="background-color: rgb(30, 30, 30)">
    <div id="tester" style="width: 1015.13px; height: 579px"></div>
    <div id="rec1"></div>
    <div id="rec2"></div>
    <div id="rec3"></div>
    <div id="rec4"></div>
    <div id="rec5"></div>
    <div id="rec6"></div>
    <div id="rec7"></div>
    <div id="rec8"></div>

    <type><span class="txt">Type</span></type>
    <outil><span class="txt">Outils d'Analyse Technique</span></outil>
    <heu><span class="txt">Temps</span></heu>
    <lastPrice><span class="txt">Last Price</span></lastPrice>
    <hourChange><span class="txt">24h Change</span></hourChange>
    <hourHigh><span class="txt">24h High</span></hourHigh>
    <hourLow><span class="txt">24h Low</span></hourLow>
    <hourVolume><span class="txt">24h Volume</span></hourVolume>
    <actualPrice><span class="txt">actualPrice</span></actualPrice>
    <sellHistoric style="white-space: nowrap"
      ><span class="txt">Historique Des Ventes</span></sellHistoric
    >
    <buyHistoric style="white-space: nowrap"
      ><span class="txt">Historique Des Achats</span></buyHistoric
    >
    <Price><span class="txt">Price</span></Price>
    <Amount><span class="txt">Amount</span></Amount>
    <Total><span class="txt">Total</span></Total>
    <Prophet><span class="txt">Modèle NeuralProphet</span></Prophet>
    <div style="text-align: center">
      <geom
        ><span class="txt" style="display: block"
          >Modèle Géométrique<br />
          Brownien</span
        ></geom
      >
    </div>
    <agentbased><span class="txt">Modèle Basé Agent</span></agentbased>
    <OAS><span class="txt">Outils d’Analyse Statistique</span></OAS>

    <!-- Create the button -->
    <button id="candle">CANDLESTICKS</button>
    <button id="classic">CLASSIC</button>
    <button id="ema">EMA</button>
    <button id="bollinger">BOLLINGER</button>
    <button id="rsi">RSI</button>
    <button id="macd">MACD</button>
    <button id="so">SO</button>
    <button id="heurea">1H</button>
    <button id="heureb">4H</button>
    <button id="sevenDay">7D</button>
    <button id="thirtyDay">30D</button>
    <button id="sixtyDay">60D</button>
    <button id="sim1">Simulation</button>
    <button id="sim2">Simulation</button>
    <button id="sim3">Simulation</button>


    <form method="POST" action="result">
        <search><input type="text" id="inputValue" name="inputValue" placeholder="Search..." class="search-bar"></search>
        <button class="image-button" id="loupe">
          <img src="loupe.png" width="25" class="my-image">
        </button>
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
        $fbrownian = file("./templates/brownian.txt", FILE_IGNORE_NEW_LINES);
        $fabsi_pred = file("./templates/absi_pred.txt", FILE_IGNORE_NEW_LINES);
    ?>
    <script>
        var candle = document.getElementById("candle");
        var classic = document.getElementById("classic");
        var ema = document.getElementById("ema");
        var bollinger = document.getElementById("bollinger");
        var rsi = document.getElementById("rsi");
        var macd = document.getElementById("macd");
        var so = document.getElementById("so");
        var heurea = document.getElementById("heurea");
        var heureb = document.getElementById("heureb");
        var sevenDay = document.getElementById("sevenDay");
        var thirtyDay = document.getElementById("thirtyDay");
        var sixtyDay = document.getElementById("sixtyDay");
        var sim1 = document.getElementById("sim1");
        var sim2 = document.getElementById("sim2");
        var sim3 = document.getElementById("sim3");


        var layout = {
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
        var brownian = JSON.parse('<?php echo json_encode($fbrownian); ?>');
        var absi_pred = JSON.parse('<?php echo json_encode($fabsi_pred); ?>');

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
        let dabsi = absi.map(function(dateString) {
          return new Date(dateString);
        });
        let dabsi_pred = absi_pred.map(function(dateString) {
          return new Date(dateString);
        });
        var cdl = false;

        function myFunctionD(x) {
          const currentDate = new Date();
          let newdate = new Date();  // create a new date object
          newdate.setDate(currentDate.getDate() - x);  // take off x days to the date
          window.filteredDates = dabsi.filter(function(date) {
            let nDate = new Date(date);
            return (nDate >= newdate && nDate <= currentDate);
          });
          window.filteredDates_pred = dabsi_pred.filter(function(date) {
            let nDate = new Date(date);
            return (nDate >= newdate);
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
          window.subbrownian = intbrownian.slice(-filteredDates_pred.length-1, -1);
        }
        myFunctionD(30);
        console.log(filteredDates)
////////////////////////////////////////////////////////////////////////////
      
        function mycandle() {
            TESTER = document.getElementById('tester');
            Plotly.newPlot( TESTER, [{
            x: filteredDates,
            open: subopen,
            high: subhigh,
            close: subclose,
            low: sublow, type: 'candlestick'}], layout);
        }
        candle.addEventListener('click', function() {
          candle.style.backgroundColor ='#546EE5';
          candle.style.color = 'white';
          classic.style.backgroundColor ='rgb(30, 30, 30)';
          classic.style.color = '#8295B2';
          ema.style.backgroundColor ='rgb(30, 30, 30)';
          ema.style.color = '#8295B2';
          bollinger.style.backgroundColor ='rgb(30, 30, 30)';
          bollinger.style.color = '#8295B2';
          macd.style.backgroundColor ='rgb(30, 30, 30)';
          macd.style.color = '#8295B2';
          rsi.style.backgroundColor ='rgb(30, 30, 30)';
          rsi.style.color = '#8295B2';
          so.style.backgroundColor ='rgb(30, 30, 30)';
          so.style.color = '#8295B2';
          sim3.style.backgroundColor ='rgb(30, 30, 30)'
          sim3.style.color = '#8295B2';
          mycandle();
          cdl = true;
        });
        
        function myplot() {
          TESTER = document.getElementById('tester');
          Plotly.newPlot( TESTER, [{
          x: filteredDates,
          y: subordo,
          line: {color: 'rgb(52, 152, 219)'}
          }], layout);
        }

        classic.addEventListener('click', function() {
          classic.style.backgroundColor ='#546EE5'
          classic.style.color = 'white';
          candle.style.backgroundColor ='rgb(30, 30, 30)';
          candle.style.color = '#8295B2';
          ema.style.backgroundColor ='rgb(30, 30, 30)';
          ema.style.color = '#8295B2';
          bollinger.style.backgroundColor ='rgb(30, 30, 30)';
          bollinger.style.color = '#8295B2';
          macd.style.backgroundColor ='rgb(30, 30, 30)';
          macd.style.color = '#8295B2';
          rsi.style.backgroundColor ='rgb(30, 30, 30)';
          rsi.style.color = '#8295B2';
          so.style.backgroundColor ='rgb(30, 30, 30)';
          so.style.color = '#8295B2';
          sim3.style.backgroundColor ='rgb(30, 30, 30)'
          sim3.style.color = '#8295B2';
          myplot();
          cdl = false;
        });

        sevenDay.addEventListener('click', function() {
          sevenDay.style.backgroundColor ='#546EE5'
          sevenDay.style.color = 'white';
          heurea.style.backgroundColor ='rgb(30, 30, 30)';
          heurea.style.color = '#8295B2';
          heureb.style.backgroundColor ='rgb(30, 30, 30)';
          heureb.style.color = '#8295B2';
          thirtyDay.style.backgroundColor ='rgb(30, 30, 30)';
          thirtyDay.style.color = '#8295B2';
          sixtyDay.style.backgroundColor ='rgb(30, 30, 30)';
          sixtyDay.style.color = '#8295B2';
          ema.style.backgroundColor ='rgb(30, 30, 30)';
          ema.style.color = '#8295B2';
          bollinger.style.backgroundColor ='rgb(30, 30, 30)';
          bollinger.style.color = '#8295B2';
          macd.style.backgroundColor ='rgb(30, 30, 30)';
          macd.style.color = '#8295B2';
          rsi.style.backgroundColor ='rgb(30, 30, 30)';
          rsi.style.color = '#8295B2';
          so.style.backgroundColor ='rgb(30, 30, 30)';
          so.style.color = '#8295B2';
          sim3.style.backgroundColor ='rgb(30, 30, 30)'
          sim3.style.color = '#8295B2';
          myFunctionD(7);
          if (cdl) {
            mycandle();
          } else {myplot();}
        });

        thirtyDay.addEventListener('click', function() {
          thirtyDay.style.backgroundColor ='#546EE5'
          thirtyDay.style.color = 'white';
          heurea.style.backgroundColor ='rgb(30, 30, 30)';
          heurea.style.color = '#8295B2';
          heureb.style.backgroundColor ='rgb(30, 30, 30)';
          heureb.style.color = '#8295B2';
          sevenDay.style.backgroundColor ='rgb(30, 30, 30)';
          sevenDay.style.color = '#8295B2';
          sixtyDay.style.backgroundColor ='rgb(30, 30, 30)';
          sixtyDay.style.color = '#8295B2';
          ema.style.backgroundColor ='rgb(30, 30, 30)';
          ema.style.color = '#8295B2';
          bollinger.style.backgroundColor ='rgb(30, 30, 30)';
          bollinger.style.color = '#8295B2';
          macd.style.backgroundColor ='rgb(30, 30, 30)';
          macd.style.color = '#8295B2';
          rsi.style.backgroundColor ='rgb(30, 30, 30)';
          rsi.style.color = '#8295B2';
          so.style.backgroundColor ='rgb(30, 30, 30)';
          so.style.color = '#8295B2';
          sim3.style.backgroundColor ='rgb(30, 30, 30)'
          sim3.style.color = '#8295B2';
          myFunctionD(30);
          if (cdl) {
            mycandle();
          } else {myplot();}
        });

        sixtyDay.addEventListener('click', function() {
          sixtyDay.style.backgroundColor ='#546EE5'
          sixtyDay.style.color = 'white';
          heurea.style.backgroundColor ='rgb(30, 30, 30)';
          heurea.style.color = '#8295B2';
          heureb.style.backgroundColor ='rgb(30, 30, 30)';
          heureb.style.color = '#8295B2';
          sevenDay.style.backgroundColor ='rgb(30, 30, 30)';
          sevenDay.style.color = '#8295B2';
          thirtyDay.style.backgroundColor ='rgb(30, 30, 30)';
          thirtyDay.style.color = '#8295B2';
          ema.style.backgroundColor ='rgb(30, 30, 30)';
          ema.style.color = '#8295B2';
          bollinger.style.backgroundColor ='rgb(30, 30, 30)';
          bollinger.style.color = '#8295B2';
          macd.style.backgroundColor ='rgb(30, 30, 30)';
          macd.style.color = '#8295B2';
          rsi.style.backgroundColor ='rgb(30, 30, 30)';
          rsi.style.color = '#8295B2';
          so.style.backgroundColor ='rgb(30, 30, 30)';
          so.style.color = '#8295B2';
          sim3.style.backgroundColor ='rgb(30, 30, 30)'
          sim3.style.color = '#8295B2';
          myFunctionD(60);
          if (cdl) {
            mycandle();
          } else {myplot();}
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
            low: sublow, type: 'candlestick'}], layout);
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
            }], layout);
          }
        }

        ema.addEventListener('click', function() {
          if (ema.style.backgroundColor == 'rgb(30, 30, 30)') {
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
            sim3.style.backgroundColor ='rgb(30, 30, 30)'
            sim3.style.color = '#8295B2';
            myewma();
          } else {
            ema.style.backgroundColor ='rgb(30, 30, 30)'
            ema.style.color = '#8295B2';
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
                sim3.style.backgroundColor ='rgb(30, 30, 30)'
                sim3.style.color = '#8295B2';
                mybollinger();
            } else {
                bollinger.style.backgroundColor ='rgb(30, 30, 30)'
                bollinger.style.color = '#8295B2';
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
            low: sublow, type: 'candlestick'}], layout);
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
            line: {color: 'rgb(52, 152, 219)'} }], layout);
          }
        }

        rsi.addEventListener('click', function() {
          if (rsi.style.backgroundColor == 'rgb(30, 30, 30)') {
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
            sim3.style.backgroundColor ='rgb(30, 30, 30)'
            sim3.style.color = '#8295B2';
            myrsi();
          } else {
            rsi.style.backgroundColor ='rgb(30, 30, 30)'
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
            }], layout);
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
            sim3.style.backgroundColor ='rgb(30, 30, 30)'
            sim3.style.color = '#8295B2';
            mymacd();
          } else {
            macd.style.backgroundColor ='rgb(30, 30, 30)'
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
            }], layout);
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
            }], layout);
          }
        }

        so.addEventListener('click', function() {
          if (so.style.backgroundColor == 'rgb(30, 30, 30)') {
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
            sim3.style.backgroundColor ='rgb(30, 30, 30)'
            sim3.style.color = '#8295B2';
            myso();
          } else {
            so.style.backgroundColor ='rgb(30, 30, 30)'
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
            }], layout);
        }

        sim3.addEventListener('click', function() {
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
            mybrownian();
          } else {
            sim3.style.backgroundColor ='rgb(30, 30, 30)'
            sim3.style.color = '#8295B2';
            if (cdl) {
              mycandle();
            } else {
              myplot();
            }
          }
        });

      myplot();
    </script>
  </body>
</html>
