/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package siif.v.demo;

import java.awt.TextField;
import java.util.Calendar;
import javax.swing.JLabel;

/**
 *
 * @author genildo.santos
 */
// Cria a nova thread
class Cronometro implements Runnable {

    Thread theadPrograma;
    TextField tempominutos;
    TextField Temposegundos;
    JLabel rotulo;
    int segundos;//em Segundos
    int minutos;

    Cronometro(JLabel rotulo, int segundos, int minutos) {
        this.rotulo = rotulo;
        this.segundos = segundos;
        this.minutos = minutos;
        
        theadPrograma = new Thread(this);// Cria a nova thread filho
        theadPrograma.start(); // Inicia a Thead
        System.out.println("Estou no novo processo.");
    }

    // Método obrigatório definido em Runnable e acionado por start()
    public void run() {
        try {
            for (int cont = 0; cont < segundos; cont++) { // Simulando um processo que consome tempo
                Thread.sleep(1000);
                int calculosegundos = segundos - cont;
                int calculominutos = minutos - cont;
                rotulo.setText(calculominutos + " : " + calculosegundos);
            }
        } catch (InterruptedException e) {
            System.out.println("Problema na execusão da Thead");
        }

        System.out.println("Fim do processo da nova Thread");
    }
}
