/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package siif.v.cronometro;

import java.time.LocalDateTime;
import siif.v.demo.CronometroTela;
import siif.v.demo.telaPrincipal;

/**
 *
 * @author fabricio
 */
public class CronometroFuncionando implements Runnable {

    public Thread theadPrograma;
    private LocalDateTime dataAtual;
    private LocalDateTime dataFutura;
    private telaPrincipal tela;

    public CronometroFuncionando(telaPrincipal tela, int minutos, int segundos) {
        this.tela = tela;
        dataAtual = LocalDateTime.now();
        dataAtual = dataAtual.withMinute(0);
        dataAtual = dataAtual.withSecond(0);
        dataAtual = dataAtual.withHour(0);
        dataFutura = LocalDateTime.of(dataAtual.getYear(), dataAtual.getMonth(), dataAtual.getDayOfMonth(), dataAtual.getHour(), dataAtual.getMinute() + minutos, dataAtual.getSecond() + segundos);

        theadPrograma = new Thread(this);// Cria a nova thread filho
        theadPrograma.start(); // Inicia a Thead

        tela.ajustarBotoes(true);
    }

    @Override
    public void run() {
        String minutosTexto = null;
        String segundosTexto = null;
        try {
            do {
                minutosTexto = String.format("%02d", dataFutura.toLocalTime().getMinute());
                segundosTexto = String.format("%02d", dataFutura.toLocalTime().getSecond());

                tela.getResultado().setText(minutosTexto + ":" + segundosTexto);
                dataFutura = dataFutura.minusSeconds(1L);
                Thread.sleep(1000);

                //Habilitar/desabilitar botões
            } while (dataFutura.isAfter(dataAtual));

            tela.getResultado().setText("00:00");
            tela.ajustarBotoes(false);

        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
    }

    public LocalDateTime getDataAtual() {
        return dataAtual;
    }

    public void setDataAtual(LocalDateTime dataAtual) {
        this.dataAtual = dataAtual;
    }

    public LocalDateTime getDataFutura() {
        return dataFutura;
    }

    public void setDataFutura(LocalDateTime dataFutura) {
        this.dataFutura = dataFutura;
    }

}
