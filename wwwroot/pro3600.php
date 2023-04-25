<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Ma page de test</title>
        <script src="https://cdn.plot.ly/plotly-2.20.0.min.js"></script>
        <style>

          #candle {
            position: absolute;
            top: 673px;
            left: 371.5px;  
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
            width: 112.5px;
            height: 32px;
          }

          #ema {
            position: absolute;
            top: 752px;
            left: 371.5px;  
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
            width: 112.5px;
            height: 32px;
          }

          #bollinger {
            position: absolute;
            top: 752px;
            left: 503px;
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
            width: 112.5px;
            height: 32px;
          }

          #rsi {
            position: absolute;
            top: 752px;
            left: 634.5px;
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
            width: 112.5px;
            height: 32px;
          }

          #macd {
            position: absolute;
            top: 752px;
            left: 766px;
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
            width: 112.5px;
            height: 32px;
          }

          #so {
            position: absolute;
            top: 752px;
            left: 897.5px;
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

          #classic {
            position: absolute;
            top: 673px;
            left: 503px;  
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
            background: #373D4C;
            border-radius: 22px;
          }

          .txt {
            font-family: 'Arial';
            font-weight: bold;
            display: flex;
            align-items: center;
            color: #8295B2;
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
            background-color: #373D4C;
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
        </style>
    </head>

    <body style="background-color: rgb(30, 30, 30);">
      <div id="tester" style="width:1015.13px;height:579px;"></div>
      
      <type><span class="txt">Type</span></type>
      <outil><span class="txt">Outils d’analyse technique</span></outil>
      <heu><span class="txt">Temps</span></heu>

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
      <button id="heurec">12H</button>

      <form method="POST" action="result">
        <search><input type="text" id="inputValue" name="inputValue" placeholder="Search..." class="search-bar"></search>
        <button class="image-button" id="loupe">
          <img src="loupe.png" width="25" class="my-image">
        </button>
      </form>

      <?php
        $fabsi = file("C:\\inetpub\\wwwroot\\absi.txt", FILE_IGNORE_NEW_LINES);
        $fordo = file("C:\\inetpub\\wwwroot\\ordo.txt", FILE_IGNORE_NEW_LINES);
      ?>

      <script>
        var candle = document.getElementById('candle');
        var classic = document.getElementById('classic');
        var ema = document.getElementById('ema');
        var bollinger = document.getElementById('bollinger');
        var rsi = document.getElementById('rsi');
        var macd = document.getElementById('macd');
        var so = document.getElementById('so');
        var heurea = document.getElementById('heurea');
        var heureb = document.getElementById('heureb');
        var heurec = document.getElementById('heurec');

        candle.addEventListener('click', function() {
          candle.style.backgroundColor ='#546EE5';
          candle.style.color = 'white';
          classic.style.backgroundColor ='rgb(30, 30, 30)';
          classic.style.color = '#8295B2';
        });

        classic.addEventListener('click', function() {
          classic.style.backgroundColor ='#546EE5'
          classic.style.color = 'white';
          candle.style.backgroundColor ='rgb(30, 30, 30)';
          candle.style.color = '#8295B2';
        });

        heurea.addEventListener('click', function() {
          heurea.style.backgroundColor ='#546EE5'
          heurea.style.color = 'white';
          heureb.style.backgroundColor ='rgb(30, 30, 30)';
          heureb.style.color = '#8295B2';
          heurec.style.backgroundColor ='rgb(30, 30, 30)';
          heurec.style.color = '#8295B2';
        });

        heureb.addEventListener('click', function() {
          heureb.style.backgroundColor ='#546EE5'
          heureb.style.color = 'white';
          heurea.style.backgroundColor ='rgb(30, 30, 30)';
          heurea.style.color = '#8295B2';
          heurec.style.backgroundColor ='rgb(30, 30, 30)';
          heurec.style.color = '#8295B2';
        });

        heurec.addEventListener('click', function() {
          heurec.style.backgroundColor ='#546EE5'
          heurec.style.color = 'white';
          heureb.style.backgroundColor ='rgb(30, 30, 30)';
          heureb.style.color = '#8295B2';
          heurea.style.backgroundColor ='rgb(30, 30, 30)';
          heurea.style.color = '#8295B2';
        });
        
        ema.addEventListener('click', function() {
          if (ema.style.backgroundColor == 'rgb(30, 30, 30)') {
            ema.style.backgroundColor ='#546EE5'
            ema.style.color = 'white';
          } else {
            ema.style.backgroundColor ='rgb(30, 30, 30)'
            ema.style.color = '#8295B2';
          }
        });

        bollinger.addEventListener('click', function() {
          if (bollinger.style.backgroundColor == 'rgb(30, 30, 30)') {
            bollinger.style.backgroundColor ='#546EE5'
            bollinger.style.color = 'white';
          } else {
            bollinger.style.backgroundColor ='rgb(30, 30, 30)'
            bollinger.style.color = '#8295B2';
          }
        });

        rsi.addEventListener('click', function() {
          if (rsi.style.backgroundColor == 'rgb(30, 30, 30)') {
            rsi.style.backgroundColor ='#546EE5'
            rsi.style.color = 'white';
          } else {
            rsi.style.backgroundColor ='rgb(30, 30, 30)'
            rsi.style.color = '#8295B2';
          }
        });

        macd.addEventListener('click', function() {
          if (macd.style.backgroundColor == 'rgb(30, 30, 30)') {
            macd.style.backgroundColor ='#546EE5'
            macd.style.color = 'white';
          } else {
            macd.style.backgroundColor ='rgb(30, 30, 30)'
            macd.style.color = '#8295B2';
          }
        });

        so.addEventListener('click', function() {
          if (so.style.backgroundColor == 'rgb(30, 30, 30)') {
            so.style.backgroundColor ='#546EE5'
            so.style.color = 'white';
          } else {
            so.style.backgroundColor ='rgb(30, 30, 30)'
            so.style.color = '#8295B2';
          }
        });

        var absi = JSON.parse('<?php echo json_encode($fabsi); ?>');
        var ordo = JSON.parse('<?php echo json_encode($fordo); ?>');
        let intordo = ordo.map(parseFloat);
        console.log(absi);
        console.log(intordo);

        var layout = {
          paper_bgcolor:'rgba(0,0,0,0)',
          plot_bgcolor:'rgba(0,0,0,0)'
        };

        TESTER = document.getElementById('tester');
        Plotly.newPlot( TESTER, [{
        x: absi,
        y: intordo }], layout);

      </script>
    </body>
</html>