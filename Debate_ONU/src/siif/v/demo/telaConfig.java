/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package siif.v.demo;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author profGenildo
 */
public class telaConfig extends javax.swing.JFrame {

    telaPrincipal tela;

    private final String arqBandeiras = "bandeiras.siif";
    private final String arqEquipes = "equipes.siif";
    private int qtdEquipe;

    /**
     * Creates new form telaConfig
     */
    public telaConfig(telaPrincipal tela) {
        initComponents();

        this.tela = tela;
        qtdEquipe = 1;
        setLocationRelativeTo(null);

        FileReader arquivo;
        try {
            arquivo = new FileReader(arqEquipes);
            BufferedReader Ler = new BufferedReader(arquivo);
            String linha = Ler.readLine();

            b01.setText(linha);
            linha = Ler.readLine();
            b02.setText(linha);
            linha = Ler.readLine();
            b03.setText(linha);
            linha = Ler.readLine();
            b04.setText(linha);
            linha = Ler.readLine();
            b05.setText(linha);
            linha = Ler.readLine();
            b06.setText(linha);
            linha = Ler.readLine();
            b07.setText(linha);
            linha = Ler.readLine();
            b08.setText(linha);
            linha = Ler.readLine();
            linha = Ler.readLine();
            b09.setText(linha);
            linha = Ler.readLine();
            b10.setText(linha);
            linha = Ler.readLine();
            b11.setText(linha);
            linha = Ler.readLine();
            b12.setText(linha);
            linha = Ler.readLine();
            b13.setText(linha);
            linha = Ler.readLine();
            b14.setText(linha);
            linha = Ler.readLine();
            b15.setText(linha);
            linha = Ler.readLine();
            b16.setText(linha);
            linha = Ler.readLine();
            b17.setText(linha);
            linha = Ler.readLine();
            b18.setText(linha);
            linha = Ler.readLine();
            b19.setText(linha);
            linha = Ler.readLine();
            b20.setText(linha);
            linha = Ler.readLine();
            b21.setText(linha);
            linha = Ler.readLine();
            b22.setText(linha);
            linha = Ler.readLine();
            b23.setText(linha);
            linha = Ler.readLine();
            b24.setText(linha);
            linha = Ler.readLine();
            b25.setText(linha);
            linha = Ler.readLine();
            b26.setText(linha);
            linha = Ler.readLine();
            b27.setText(linha);
            linha = Ler.readLine();
            b28.setText(linha);
            linha = Ler.readLine();
            b29.setText(linha);
            linha = Ler.readLine();
            b30.setText(linha);
            linha = Ler.readLine();
            b31.setText(linha);
            linha = Ler.readLine();
            b32.setText(linha);
            linha = Ler.readLine();
            b33.setText(linha);
            linha = Ler.readLine();
            b34.setText(linha);
            linha = Ler.readLine();
            b35.setText(linha);
            linha = Ler.readLine();
            b36.setText(linha);
            linha = Ler.readLine();

            Ler.close();
            arquivo.close();

            arquivo = new FileReader(arqBandeiras);
            Ler = new BufferedReader(arquivo);
            linha = Ler.readLine();

            b01.setSelected(converte(linha));
            linha = Ler.readLine();
            b02.setSelected(converte(linha));
            linha = Ler.readLine();
            b03.setSelected(converte(linha));
            linha = Ler.readLine();
            b04.setSelected(converte(linha));
            linha = Ler.readLine();
            b05.setSelected(converte(linha));
            linha = Ler.readLine();
            b06.setSelected(converte(linha));
            linha = Ler.readLine();
            b07.setSelected(converte(linha));
            linha = Ler.readLine();
            b08.setSelected(converte(linha));
            linha = Ler.readLine();
            b09.setSelected(converte(linha));
            linha = Ler.readLine();
            b10.setSelected(converte(linha));
            linha = Ler.readLine();
            b11.setSelected(converte(linha));
            linha = Ler.readLine();
            b12.setSelected(converte(linha));
            linha = Ler.readLine();
            b13.setSelected(converte(linha));
            linha = Ler.readLine();
            b14.setSelected(converte(linha));
            linha = Ler.readLine();
            b15.setSelected(converte(linha));
            linha = Ler.readLine();
            b16.setSelected(converte(linha));
            linha = Ler.readLine();
            b17.setSelected(converte(linha));
            linha = Ler.readLine();
            b18.setSelected(converte(linha));
            linha = Ler.readLine();
            b19.setSelected(converte(linha));
            linha = Ler.readLine();
            b20.setSelected(converte(linha));
            linha = Ler.readLine();
            b21.setSelected(converte(linha));
            linha = Ler.readLine();
            b22.setSelected(converte(linha));
            linha = Ler.readLine();
            b23.setSelected(converte(linha));
            linha = Ler.readLine();
            b24.setSelected(converte(linha));
            linha = Ler.readLine();
            b25.setSelected(converte(linha));
            linha = Ler.readLine();
            b26.setSelected(converte(linha));
            linha = Ler.readLine();
            b27.setSelected(converte(linha));
            linha = Ler.readLine();
            b28.setSelected(converte(linha));
            linha = Ler.readLine();
            b29.setSelected(converte(linha));
            linha = Ler.readLine();
            b30.setSelected(converte(linha));
            linha = Ler.readLine();
            b31.setSelected(converte(linha));
            linha = Ler.readLine();
            b32.setSelected(converte(linha));
            linha = Ler.readLine();
            b33.setSelected(converte(linha));
            linha = Ler.readLine();
            b34.setSelected(converte(linha));
            linha = Ler.readLine();
            b35.setSelected(converte(linha));
            linha = Ler.readLine();
            b36.setSelected(converte(linha));
            linha = Ler.readLine();

            Ler.close();
            arquivo.close();

            qtdEquipe = qtdEquipeAtiva();
            lblQuantidade.setText("Total selecionado: " + qtdEquipe);

        } catch (FileNotFoundException ex) {
            Logger.getLogger(telaConfig.class.getName()).log(Level.SEVERE, null, ex);
        } catch (IOException ex) {
            Logger.getLogger(telaConfig.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

    private int qtdEquipeAtiva() {
        int qtd = 0;

        if (b01.isSelected()) {
            qtd++;
        }
        if (b02.isSelected()) {
            qtd++;
        }
        if (b03.isSelected()) {
            qtd++;
        }
        if (b04.isSelected()) {
            qtd++;
        }
        if (b05.isSelected()) {
            qtd++;
        }
        if (b06.isSelected()) {
            qtd++;
        }
        if (b07.isSelected()) {
            qtd++;
        }
        if (b08.isSelected()) {
            qtd++;
        }
        if (b09.isSelected()) {
            qtd++;
        }
        if (b10.isSelected()) {
            qtd++;
        }
        if (b11.isSelected()) {
            qtd++;
        }
        if (b12.isSelected()) {
            qtd++;
        }
        if (b13.isSelected()) {
            qtd++;
        }
        if (b14.isSelected()) {
            qtd++;
        }
        if (b15.isSelected()) {
            qtd++;
        }
        if (b16.isSelected()) {
            qtd++;
        }
        if (b17.isSelected()) {
            qtd++;
        }
        if (b18.isSelected()) {
            qtd++;
        }
        if (b19.isSelected()) {
            qtd++;
        }
        if (b20.isSelected()) {
            qtd++;
        }
        if (b21.isSelected()) {
            qtd++;
        }
        if (b22.isSelected()) {
            qtd++;
        }
        if (b23.isSelected()) {
            qtd++;
        }
        if (b24.isSelected()) {
            qtd++;
        }
        if (b25.isSelected()) {
            qtd++;
        }
        if (b26.isSelected()) {
            qtd++;
        }
        if (b27.isSelected()) {
            qtd++;
        }
        if (b28.isSelected()) {
            qtd++;
        }
        if (b29.isSelected()) {
            qtd++;
        }
        if (b30.isSelected()) {
            qtd++;
        }
        if (b31.isSelected()) {
            qtd++;
        }
        if (b32.isSelected()) {
            qtd++;
        }
        if (b33.isSelected()) {
            qtd++;
        }
        if (b34.isSelected()) {
            qtd++;
        }
        if (b35.isSelected()) {
            qtd++;
        }
        if (b36.isSelected()) {
            qtd++;
        }

        return qtd;
    }

    private boolean converte(String valor) {
        return valor.equals("true");
    }

    private void atualizaQtdEquipe(boolean ativo) {
        if (ativo) {
            qtdEquipe++;
        } else {
            qtdEquipe--;
        }

        lblQuantidade.setText("Total selecionado: " + qtdEquipe);
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        b04 = new javax.swing.JCheckBox();
        b02 = new javax.swing.JCheckBox();
        b01 = new javax.swing.JCheckBox();
        b03 = new javax.swing.JCheckBox();
        b05 = new javax.swing.JCheckBox();
        b06 = new javax.swing.JCheckBox();
        b07 = new javax.swing.JCheckBox();
        b08 = new javax.swing.JCheckBox();
        b09 = new javax.swing.JCheckBox();
        b10 = new javax.swing.JCheckBox();
        b11 = new javax.swing.JCheckBox();
        b12 = new javax.swing.JCheckBox();
        b13 = new javax.swing.JCheckBox();
        b14 = new javax.swing.JCheckBox();
        b15 = new javax.swing.JCheckBox();
        b16 = new javax.swing.JCheckBox();
        b17 = new javax.swing.JCheckBox();
        b18 = new javax.swing.JCheckBox();
        lblQuantidade = new javax.swing.JLabel();
        lbl01 = new javax.swing.JLabel();
        lbl02 = new javax.swing.JLabel();
        lbl03 = new javax.swing.JLabel();
        lbl04 = new javax.swing.JLabel();
        lbl05 = new javax.swing.JLabel();
        lbl06 = new javax.swing.JLabel();
        lbl07 = new javax.swing.JLabel();
        lbl08 = new javax.swing.JLabel();
        lbl09 = new javax.swing.JLabel();
        lbl10 = new javax.swing.JLabel();
        lbl11 = new javax.swing.JLabel();
        lbl12 = new javax.swing.JLabel();
        lbl13 = new javax.swing.JLabel();
        lbl14 = new javax.swing.JLabel();
        lbl15 = new javax.swing.JLabel();
        lbl16 = new javax.swing.JLabel();
        lbl17 = new javax.swing.JLabel();
        lbl18 = new javax.swing.JLabel();
        jButton1 = new javax.swing.JButton();
        jButton2 = new javax.swing.JButton();
        jButton3 = new javax.swing.JButton();
        lblAviso = new javax.swing.JLabel();
        btnGravar = new javax.swing.JButton();
        jButton4 = new javax.swing.JButton();
        b22 = new javax.swing.JCheckBox();
        b20 = new javax.swing.JCheckBox();
        b19 = new javax.swing.JCheckBox();
        b21 = new javax.swing.JCheckBox();
        b23 = new javax.swing.JCheckBox();
        b24 = new javax.swing.JCheckBox();
        b25 = new javax.swing.JCheckBox();
        b26 = new javax.swing.JCheckBox();
        b27 = new javax.swing.JCheckBox();
        b28 = new javax.swing.JCheckBox();
        b29 = new javax.swing.JCheckBox();
        b30 = new javax.swing.JCheckBox();
        b31 = new javax.swing.JCheckBox();
        b32 = new javax.swing.JCheckBox();
        b33 = new javax.swing.JCheckBox();
        b34 = new javax.swing.JCheckBox();
        b35 = new javax.swing.JCheckBox();
        b36 = new javax.swing.JCheckBox();
        lbl19 = new javax.swing.JLabel();
        lbl20 = new javax.swing.JLabel();
        lbl21 = new javax.swing.JLabel();
        lbl22 = new javax.swing.JLabel();
        lbl24 = new javax.swing.JLabel();
        lbl23 = new javax.swing.JLabel();
        lbl25 = new javax.swing.JLabel();
        lbl26 = new javax.swing.JLabel();
        lbl27 = new javax.swing.JLabel();
        lbl28 = new javax.swing.JLabel();
        lbl29 = new javax.swing.JLabel();
        lbl30 = new javax.swing.JLabel();
        lbl31 = new javax.swing.JLabel();
        lbl32 = new javax.swing.JLabel();
        lbl33 = new javax.swing.JLabel();
        lbl34 = new javax.swing.JLabel();
        lbl35 = new javax.swing.JLabel();
        lbl37 = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setPreferredSize(new java.awt.Dimension(1366, 700));

        jLabel1.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        jLabel1.setText("Escolha os países para o sorteio:");

        b04.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b04ActionPerformed(evt);
            }
        });

        b02.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b02ActionPerformed(evt);
            }
        });

        b01.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b01ActionPerformed(evt);
            }
        });

        b03.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b03ActionPerformed(evt);
            }
        });

        b05.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b05ActionPerformed(evt);
            }
        });

        b06.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b06ActionPerformed(evt);
            }
        });

        b07.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b07ActionPerformed(evt);
            }
        });

        b08.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b08ActionPerformed(evt);
            }
        });

        b09.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b09ActionPerformed(evt);
            }
        });

        b10.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b10ActionPerformed(evt);
            }
        });

        b11.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b11ActionPerformed(evt);
            }
        });

        b12.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b12ActionPerformed(evt);
            }
        });

        b13.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b13ActionPerformed(evt);
            }
        });

        b14.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b14ActionPerformed(evt);
            }
        });

        b15.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b15ActionPerformed(evt);
            }
        });

        b16.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b16ActionPerformed(evt);
            }
        });

        b17.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b17ActionPerformed(evt);
            }
        });

        b18.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b18ActionPerformed(evt);
            }
        });

        lblQuantidade.setFont(new java.awt.Font("Tahoma", 0, 12)); // NOI18N
        lblQuantidade.setText("Total selecionado: 1");

        lbl01.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b01_.png"))); // NOI18N

        lbl02.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b02_.png"))); // NOI18N

        lbl03.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b03_.png"))); // NOI18N

        lbl04.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b04_.png"))); // NOI18N

        lbl05.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b25_.png"))); // NOI18N

        lbl06.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b31_.png"))); // NOI18N

        lbl07.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b05_.png"))); // NOI18N

        lbl08.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b06_.png"))); // NOI18N

        lbl09.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b07_.png"))); // NOI18N

        lbl10.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b08_.png"))); // NOI18N

        lbl11.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b26_.png"))); // NOI18N

        lbl12.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b32_.png"))); // NOI18N

        lbl13.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b09_.png"))); // NOI18N

        lbl14.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b10_.png"))); // NOI18N

        lbl15.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b11_.png"))); // NOI18N

        lbl16.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b12_.png"))); // NOI18N

        lbl17.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b27_.png"))); // NOI18N

        lbl18.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b33_.png"))); // NOI18N

        jButton1.setText("Marcar todos.");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        jButton2.setText("Desmarcar todos.");
        jButton2.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton2ActionPerformed(evt);
            }
        });

        jButton3.setText("Gerar sorteio");
        jButton3.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton3ActionPerformed(evt);
            }
        });

        lblAviso.setFont(new java.awt.Font("Tahoma", 1, 12)); // NOI18N
        lblAviso.setForeground(new java.awt.Color(255, 51, 51));
        lblAviso.setText("Aguardando sorteio...");

        btnGravar.setText("Usar e gravar este sorteio?");
        btnGravar.setEnabled(false);
        btnGravar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                btnGravarActionPerformed(evt);
            }
        });

        jButton4.setText("Fechar");
        jButton4.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton4ActionPerformed(evt);
            }
        });

        b22.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b22ActionPerformed(evt);
            }
        });

        b20.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b20ActionPerformed(evt);
            }
        });

        b19.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b19ActionPerformed(evt);
            }
        });

        b21.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b21ActionPerformed(evt);
            }
        });

        b23.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b23ActionPerformed(evt);
            }
        });

        b24.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b24ActionPerformed(evt);
            }
        });

        b25.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b25ActionPerformed(evt);
            }
        });

        b26.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b26ActionPerformed(evt);
            }
        });

        b27.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b27ActionPerformed(evt);
            }
        });

        b28.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b28ActionPerformed(evt);
            }
        });

        b29.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b29ActionPerformed(evt);
            }
        });

        b30.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b30ActionPerformed(evt);
            }
        });

        b31.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b31ActionPerformed(evt);
            }
        });

        b32.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b32ActionPerformed(evt);
            }
        });

        b33.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b33ActionPerformed(evt);
            }
        });

        b34.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b34ActionPerformed(evt);
            }
        });

        b35.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b35ActionPerformed(evt);
            }
        });

        b36.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                b36ActionPerformed(evt);
            }
        });

        lbl19.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b13_.png"))); // NOI18N

        lbl20.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b14_.png"))); // NOI18N

        lbl21.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b15_.png"))); // NOI18N

        lbl22.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b16_.png"))); // NOI18N

        lbl24.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b37_.png"))); // NOI18N

        lbl23.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b28_.png"))); // NOI18N

        lbl25.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b17_.png"))); // NOI18N

        lbl26.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b18_.png"))); // NOI18N

        lbl27.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b19_.png"))); // NOI18N

        lbl28.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b20_.png"))); // NOI18N

        lbl29.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b29_.png"))); // NOI18N

        lbl30.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b35_.png"))); // NOI18N

        lbl31.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b21_.png"))); // NOI18N

        lbl32.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b22_.png"))); // NOI18N

        lbl33.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b23_.png"))); // NOI18N

        lbl34.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b24_.png"))); // NOI18N

        lbl35.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b30_.png"))); // NOI18N

        lbl37.setIcon(new javax.swing.ImageIcon(getClass().getResource("/imagem/b36_.png"))); // NOI18N

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(20, 20, 20)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jButton3)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(btnGravar)
                        .addGap(360, 360, 360)
                        .addComponent(jButton4))
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(lblQuantidade)
                                .addGap(18, 18, 18)
                                .addComponent(lblAviso, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(jLabel1)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addComponent(jButton1)
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addComponent(jButton2))
                                    .addComponent(b02)
                                    .addComponent(b04)
                                    .addComponent(lbl04)
                                    .addComponent(b03)
                                    .addComponent(lbl03)
                                    .addGroup(layout.createSequentialGroup()
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addGroup(layout.createSequentialGroup()
                                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                    .addComponent(lbl01)
                                                    .addComponent(b01)
                                                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                            .addComponent(b05)
                                                            .addComponent(lbl05, javax.swing.GroupLayout.Alignment.TRAILING))
                                                        .addComponent(b06)
                                                        .addComponent(lbl06, javax.swing.GroupLayout.Alignment.TRAILING)))
                                                .addGap(10, 10, 10))
                                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                                .addComponent(lbl02)
                                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)))
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addComponent(b12)
                                            .addGroup(layout.createSequentialGroup()
                                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                    .addComponent(lbl11)
                                                    .addComponent(b11)
                                                    .addGroup(layout.createSequentialGroup()
                                                        .addGap(2, 2, 2)
                                                        .addComponent(lbl12)))
                                                .addGap(10, 10, 10)
                                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                    .addComponent(b18)
                                                    .addComponent(lbl18)
                                                    .addComponent(lbl17)
                                                    .addComponent(b17)))
                                            .addGroup(layout.createSequentialGroup()
                                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                    .addGroup(layout.createSequentialGroup()
                                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                            .addComponent(lbl07)
                                                            .addComponent(lbl09)
                                                            .addComponent(lbl10)
                                                            .addComponent(b07)
                                                            .addComponent(b10)
                                                            .addComponent(b09)
                                                            .addComponent(b08))
                                                        .addGap(10, 10, 10))
                                                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                                                        .addComponent(lbl08)
                                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)))
                                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                                    .addComponent(b14)
                                                    .addComponent(b15)
                                                    .addComponent(b16)
                                                    .addComponent(lbl16)
                                                    .addComponent(lbl15)
                                                    .addComponent(lbl14)
                                                    .addComponent(lbl13)
                                                    .addComponent(b13))))))
                                .addGap(10, 10, 10)))
                        .addGap(0, 0, 0)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addGroup(layout.createSequentialGroup()
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 4, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addComponent(lbl20))
                            .addComponent(b20)
                            .addComponent(b22)
                            .addComponent(lbl22)
                            .addComponent(b21)
                            .addComponent(lbl21)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(lbl19)
                                    .addComponent(b19))
                                .addGap(10, 10, 10)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(lbl25)
                                    .addComponent(lbl26)
                                    .addComponent(lbl27)
                                    .addComponent(lbl28)
                                    .addComponent(b25)
                                    .addComponent(b28)
                                    .addComponent(b27)
                                    .addComponent(b26))
                                .addGap(10, 10, 10)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(b32)
                                    .addComponent(b33)
                                    .addComponent(b34)
                                    .addComponent(lbl34)
                                    .addComponent(lbl33)
                                    .addComponent(lbl32)
                                    .addComponent(lbl31)
                                    .addComponent(b31)))
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                        .addComponent(b23)
                                        .addComponent(lbl23, javax.swing.GroupLayout.Alignment.TRAILING))
                                    .addComponent(b24)
                                    .addComponent(lbl24, javax.swing.GroupLayout.Alignment.TRAILING))
                                .addGap(10, 10, 10)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(b30)
                                    .addComponent(b29)
                                    .addGroup(layout.createSequentialGroup()
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addComponent(lbl30)
                                            .addComponent(lbl29))
                                        .addGap(12, 12, 12)
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addComponent(b35)
                                            .addComponent(lbl37)
                                            .addComponent(lbl35)
                                            .addComponent(b36))))))))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel1)
                            .addComponent(jButton1)
                            .addComponent(jButton2))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(b01, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(b07, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(lbl07)
                                    .addComponent(lbl01)
                                    .addComponent(lbl13)))
                            .addComponent(b13, javax.swing.GroupLayout.PREFERRED_SIZE, 17, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                        .addGroup(layout.createSequentialGroup()
                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                .addComponent(b19, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addComponent(b25, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                .addComponent(lbl25)
                                .addComponent(lbl19)
                                .addComponent(lbl31)))
                        .addComponent(b31, javax.swing.GroupLayout.PREFERRED_SIZE, 17, javax.swing.GroupLayout.PREFERRED_SIZE)))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(b02, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(b08, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(lbl02)
                                    .addComponent(lbl08)
                                    .addComponent(lbl14)))
                            .addComponent(b14, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(b03, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(b09, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(lbl03)
                                    .addComponent(lbl09)
                                    .addComponent(lbl15)))
                            .addComponent(b15, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(22, 22, 22)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(b04, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(b10, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(lbl04)
                                    .addComponent(lbl10)
                                    .addComponent(lbl16)))
                            .addComponent(b16, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(b05, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(b11, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                        .addGroup(layout.createSequentialGroup()
                                            .addComponent(lbl17)
                                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                            .addComponent(b18, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                            .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                            .addComponent(lbl18))
                                        .addGroup(layout.createSequentialGroup()
                                            .addComponent(lbl11, javax.swing.GroupLayout.PREFERRED_SIZE, 35, javax.swing.GroupLayout.PREFERRED_SIZE)
                                            .addGap(40, 40, 40)
                                            .addComponent(lbl12)))
                                    .addGroup(layout.createSequentialGroup()
                                        .addComponent(lbl05)
                                        .addGap(18, 18, 18)
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                            .addComponent(b06, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                            .addComponent(b12, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                        .addComponent(lbl06))))
                            .addComponent(b17, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(b20, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(b26, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(lbl20)
                                    .addComponent(lbl26)
                                    .addComponent(lbl32)))
                            .addComponent(b32, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(b21, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(b27, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(lbl21)
                                    .addComponent(lbl27)
                                    .addComponent(lbl33)))
                            .addComponent(b33, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(22, 22, 22)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                .addComponent(b22, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addComponent(b28, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addComponent(b34, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(lbl22)
                            .addComponent(lbl28)
                            .addComponent(lbl34))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                .addComponent(b23, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addComponent(b29, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                            .addComponent(b35, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                .addGroup(layout.createSequentialGroup()
                                    .addComponent(lbl35)
                                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                    .addComponent(b36, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                    .addComponent(lbl37))
                                .addGroup(layout.createSequentialGroup()
                                    .addComponent(lbl29, javax.swing.GroupLayout.PREFERRED_SIZE, 35, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addGap(18, 18, 18)
                                    .addComponent(b30, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                    .addComponent(lbl30)))
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(lbl23)
                                .addGap(18, 18, 18)
                                .addComponent(b24, javax.swing.GroupLayout.PREFERRED_SIZE, 16, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(lbl24)))))
                .addGap(60, 60, 60)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(lblQuantidade)
                    .addComponent(lblAviso))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jButton3)
                    .addComponent(btnGravar)
                    .addComponent(jButton4))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void b01ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b01ActionPerformed
        atualizaQtdEquipe(b01.isSelected());
    }//GEN-LAST:event_b01ActionPerformed

    private void b02ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b02ActionPerformed
        atualizaQtdEquipe(b02.isSelected());
    }//GEN-LAST:event_b02ActionPerformed

    private void b03ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b03ActionPerformed
        atualizaQtdEquipe(b03.isSelected());
    }//GEN-LAST:event_b03ActionPerformed

    private void b04ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b04ActionPerformed
        atualizaQtdEquipe(b04.isSelected());
    }//GEN-LAST:event_b04ActionPerformed

    private void b05ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b05ActionPerformed
        atualizaQtdEquipe(b05.isSelected());
    }//GEN-LAST:event_b05ActionPerformed

    private void b06ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b06ActionPerformed
        atualizaQtdEquipe(b06.isSelected());
    }//GEN-LAST:event_b06ActionPerformed

    private void b07ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b07ActionPerformed
        atualizaQtdEquipe(b07.isSelected());
    }//GEN-LAST:event_b07ActionPerformed

    private void b08ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b08ActionPerformed
        atualizaQtdEquipe(b08.isSelected());
    }//GEN-LAST:event_b08ActionPerformed

    private void b09ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b09ActionPerformed
        atualizaQtdEquipe(b09.isSelected());
    }//GEN-LAST:event_b09ActionPerformed

    private void b10ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b10ActionPerformed
        atualizaQtdEquipe(b10.isSelected());
    }//GEN-LAST:event_b10ActionPerformed

    private void b11ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b11ActionPerformed
        atualizaQtdEquipe(b11.isSelected());
    }//GEN-LAST:event_b11ActionPerformed

    private void b12ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b12ActionPerformed
        atualizaQtdEquipe(b12.isSelected());
    }//GEN-LAST:event_b12ActionPerformed

    private void b13ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b13ActionPerformed
        atualizaQtdEquipe(b13.isSelected());
    }//GEN-LAST:event_b13ActionPerformed

    private void b14ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b14ActionPerformed
        atualizaQtdEquipe(b14.isSelected());
    }//GEN-LAST:event_b14ActionPerformed

    private void b15ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b15ActionPerformed
        atualizaQtdEquipe(b15.isSelected());
    }//GEN-LAST:event_b15ActionPerformed

    private void b16ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b16ActionPerformed
        atualizaQtdEquipe(b16.isSelected());
    }//GEN-LAST:event_b16ActionPerformed

    private void b17ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b17ActionPerformed
        atualizaQtdEquipe(b17.isSelected());
    }//GEN-LAST:event_b17ActionPerformed

    private void b18ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b18ActionPerformed
        atualizaQtdEquipe(b18.isSelected());
    }//GEN-LAST:event_b18ActionPerformed

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        lblQuantidade.setText("Total selecionado: 36");
        qtdEquipe = 36;

        b01.setSelected(true);
        b02.setSelected(true);
        b03.setSelected(true);
        b04.setSelected(true);
        b05.setSelected(true);
        b06.setSelected(true);
        b07.setSelected(true);
        b08.setSelected(true);
        b09.setSelected(true);
        b10.setSelected(true);
        b11.setSelected(true);
        b12.setSelected(true);
        b13.setSelected(true);
        b14.setSelected(true);
        b15.setSelected(true);
        b16.setSelected(true);
        b17.setSelected(true);
        b18.setSelected(true);
        b19.setSelected(true);
        b20.setSelected(true);
        b21.setSelected(true);
        b22.setSelected(true);
        b23.setSelected(true);
        b24.setSelected(true);
        b25.setSelected(true);
        b26.setSelected(true);
        b27.setSelected(true);
        b28.setSelected(true);
        b29.setSelected(true);
        b30.setSelected(true);
        b31.setSelected(true);
        b32.setSelected(true);
        b33.setSelected(true);
        b34.setSelected(true);
        b35.setSelected(true);
        b36.setSelected(true);
    }//GEN-LAST:event_jButton1ActionPerformed

    private void jButton2ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton2ActionPerformed
        lblQuantidade.setText("Total selecionado: 0");
        qtdEquipe = 0;

        b01.setSelected(false);
        b02.setSelected(false);
        b03.setSelected(false);
        b04.setSelected(false);
        b05.setSelected(false);
        b06.setSelected(false);
        b07.setSelected(false);
        b08.setSelected(false);
        b09.setSelected(false);
        b10.setSelected(false);
        b11.setSelected(false);
        b12.setSelected(false);
        b13.setSelected(false);
        b14.setSelected(false);
        b15.setSelected(false);
        b16.setSelected(false);
        b17.setSelected(false);
        b18.setSelected(false);
        b19.setSelected(false);
        b20.setSelected(false);
        b21.setSelected(false);
        b22.setSelected(false);
        b23.setSelected(false);
        b24.setSelected(false);
        b25.setSelected(false);
        b26.setSelected(false);
        b27.setSelected(false);
        b28.setSelected(false);
        b29.setSelected(false);
        b30.setSelected(false);
        b31.setSelected(false);
        b32.setSelected(false);
        b33.setSelected(false);
        b34.setSelected(false);
        b35.setSelected(false);
        b36.setSelected(false);
    }//GEN-LAST:event_jButton2ActionPerformed

    private int randomizaIntervalo(int inicio, int fim) {
        int valor = (int) (Math.random() * fim - 0.01);
        if (valor < inicio) {
            valor = (inicio - valor) + valor;
        }

        return valor;
    }

    private void sortear(int quantidade, int inicio, int fim) {
        String resultado = "";
        List<Integer> resultados = new ArrayList<Integer>();
        int valorSorteado = 0;
        int proximoPais = 1;
        for (int cont = 1; cont <= quantidade; cont++) {
            valorSorteado = randomizaIntervalo(inicio, fim);

            while (resultados.contains(valorSorteado)) {
                valorSorteado = randomizaIntervalo(inicio, fim);
            }

            proximoPais = registrarTelaEquipe(proximoPais, valorSorteado) + 1;

            resultados.add(valorSorteado);

            resultado = resultado + Integer.toString(valorSorteado) + ";";
        }
    }

    private int registrarTelaEquipe(int ultimoPais, int equipe) {
        int pais;
        boolean achou = false;
        for (pais = ultimoPais; pais <= 36; pais++) {
            switch (pais) {
                case 1:
                    if (b01.isSelected()) {
                        b01.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 2:
                    if (b02.isSelected()) {
                        b02.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 3:
                    if (b03.isSelected()) {
                        b03.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 4:
                    if (b04.isSelected()) {
                        b04.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 5:
                    if (b05.isSelected()) {
                        b05.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 6:
                    if (b06.isSelected()) {
                        b06.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 7:
                    if (b07.isSelected()) {
                        b07.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 8:
                    if (b08.isSelected()) {
                        b08.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 9:
                    if (b09.isSelected()) {
                        b09.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 10:
                    if (b10.isSelected()) {
                        b10.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 11:
                    if (b11.isSelected()) {
                        b11.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 12:
                    if (b12.isSelected()) {
                        b12.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 13:
                    if (b13.isSelected()) {
                        b13.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 14:
                    if (b14.isSelected()) {
                        b14.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 15:
                    if (b15.isSelected()) {
                        b15.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 16:
                    if (b16.isSelected()) {
                        b16.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 17:
                    if (b17.isSelected()) {
                        b17.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 18:
                    if (b18.isSelected()) {
                        b18.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 19:
                    if (b19.isSelected()) {
                        b19.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 20:
                    if (b20.isSelected()) {
                        b20.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 21:
                    if (b21.isSelected()) {
                        b21.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 22:
                    if (b22.isSelected()) {
                        b22.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 23:
                    if (b23.isSelected()) {
                        b23.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 24:
                    if (b24.isSelected()) {
                        b24.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 25:
                    if (b25.isSelected()) {
                        b25.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 26:
                    if (b26.isSelected()) {
                        b26.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 27:
                    if (b27.isSelected()) {
                        b27.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 28:
                    if (b28.isSelected()) {
                        b28.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 29:
                    if (b29.isSelected()) {
                        b29.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 30:
                    if (b30.isSelected()) {
                        b30.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 31:
                    if (b31.isSelected()) {
                        b31.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 32:
                    if (b32.isSelected()) {
                        b32.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 33:
                    if (b33.isSelected()) {
                        b33.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 34:
                    if (b34.isSelected()) {
                        b34.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 35:
                    if (b35.isSelected()) {
                        b35.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

                case 36:
                    if (b36.isSelected()) {
                        b36.setText("Equipe: " + equipe);
                        achou = true;
                    }
                    break;

            }

            if (achou) {
                break;
            }
        }

        return pais;
    }

    private void jButton3ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton3ActionPerformed
        b01.setText("");
        b02.setText("");
        b03.setText("");
        b04.setText("");
        b05.setText("");
        b06.setText("");
        b07.setText("");
        b08.setText("");
        b09.setText("");
        b10.setText("");
        b11.setText("");
        b12.setText("");
        b13.setText("");
        b14.setText("");
        b15.setText("");
        b16.setText("");
        b17.setText("");
        b18.setText("");
        b19.setText("");
        b20.setText("");
        b21.setText("");
        b22.setText("");
        b23.setText("");
        b24.setText("");
        b25.setText("");
        b26.setText("");
        b27.setText("");
        b28.setText("");
        b29.setText("");
        b30.setText("");
        b31.setText("");
        b32.setText("");
        b33.setText("");
        b34.setText("");
        b35.setText("");
        b36.setText("");

        if (qtdEquipe <= 1) {
            lblAviso.setText("Não é possível realizar sorteio. Por gentileza, selecione mais países.");
            btnGravar.setEnabled(false);
        } else {
            btnGravar.setEnabled(true);
            lblAviso.setText("Sorteio realizado com sucesso :)");
            sortear(qtdEquipe, 1, qtdEquipe + 1);
        }
    }//GEN-LAST:event_jButton3ActionPerformed

    private void btnGravarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_btnGravarActionPerformed
        FileWriter arquivo;
        try {
            arquivo = new FileWriter(arqBandeiras, false);
            PrintWriter Escreve = new PrintWriter(arquivo);

            Escreve.println(b01.isSelected());
            Escreve.println(b02.isSelected());
            Escreve.println(b03.isSelected());
            Escreve.println(b04.isSelected());
            Escreve.println(b05.isSelected());
            Escreve.println(b06.isSelected());
            Escreve.println(b07.isSelected());
            Escreve.println(b08.isSelected());
            Escreve.println(b09.isSelected());
            Escreve.println(b10.isSelected());
            Escreve.println(b11.isSelected());
            Escreve.println(b12.isSelected());
            Escreve.println(b13.isSelected());
            Escreve.println(b14.isSelected());
            Escreve.println(b15.isSelected());
            Escreve.println(b16.isSelected());
            Escreve.println(b17.isSelected());
            Escreve.println(b18.isSelected());
            Escreve.println(b19.isSelected());
            Escreve.println(b20.isSelected());
            Escreve.println(b21.isSelected());
            Escreve.println(b22.isSelected());
            Escreve.println(b23.isSelected());
            Escreve.println(b24.isSelected());
            Escreve.println(b25.isSelected());
            Escreve.println(b26.isSelected());
            Escreve.println(b27.isSelected());
            Escreve.println(b28.isSelected());
            Escreve.println(b29.isSelected());
            Escreve.println(b30.isSelected());
            Escreve.println(b31.isSelected());
            Escreve.println(b32.isSelected());
            Escreve.println(b33.isSelected());
            Escreve.println(b34.isSelected());
            Escreve.println(b35.isSelected());
            Escreve.println(b36.isSelected());

            Escreve.close();
            arquivo.close();

            arquivo = new FileWriter(arqEquipes, false);
            Escreve = new PrintWriter(arquivo);

            Escreve.println(b01.getText());
            Escreve.println(b02.getText());
            Escreve.println(b03.getText());
            Escreve.println(b04.getText());
            Escreve.println(b05.getText());
            Escreve.println(b06.getText());
            Escreve.println(b07.getText());
            Escreve.println(b08.getText());
            Escreve.println(b09.getText());
            Escreve.println(b10.getText());
            Escreve.println(b11.getText());
            Escreve.println(b12.getText());
            Escreve.println(b13.getText());
            Escreve.println(b14.getText());
            Escreve.println(b15.getText());
            Escreve.println(b16.getText());
            Escreve.println(b17.getText());
            Escreve.println(b18.getText());
            Escreve.println(b19.getText());
            Escreve.println(b20.getText());
            Escreve.println(b21.getText());
            Escreve.println(b22.getText());
            Escreve.println(b23.getText());
            Escreve.println(b24.getText());
            Escreve.println(b25.getText());
            Escreve.println(b26.getText());
            Escreve.println(b27.getText());
            Escreve.println(b28.getText());
            Escreve.println(b29.getText());
            Escreve.println(b30.getText());
            Escreve.println(b31.getText());
            Escreve.println(b32.getText());
            Escreve.println(b33.getText());
            Escreve.println(b34.getText());
            Escreve.println(b35.getText());
            Escreve.println(b36.getText());

            Escreve.close();
            arquivo.close();

            lblAviso.setText("Configuração salva.");

            tela.ajustarBandeiras();
            //tela.repaint();
        } catch (IOException ex) {
            lblAviso.setText("Erro ao gravar: " + ex.getMessage());
        }

    }//GEN-LAST:event_btnGravarActionPerformed

    private void jButton4ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton4ActionPerformed
        this.dispose();
    }//GEN-LAST:event_jButton4ActionPerformed

    private void b22ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b22ActionPerformed
        atualizaQtdEquipe(b22.isSelected());
    }//GEN-LAST:event_b22ActionPerformed

    private void b20ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b20ActionPerformed
        atualizaQtdEquipe(b20.isSelected());
    }//GEN-LAST:event_b20ActionPerformed

    private void b19ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b19ActionPerformed
        atualizaQtdEquipe(b19.isSelected());
    }//GEN-LAST:event_b19ActionPerformed

    private void b21ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b21ActionPerformed
        atualizaQtdEquipe(b21.isSelected());
    }//GEN-LAST:event_b21ActionPerformed

    private void b23ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b23ActionPerformed
        atualizaQtdEquipe(b23.isSelected());
    }//GEN-LAST:event_b23ActionPerformed

    private void b24ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b24ActionPerformed
        atualizaQtdEquipe(b24.isSelected());
    }//GEN-LAST:event_b24ActionPerformed

    private void b25ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b25ActionPerformed
        atualizaQtdEquipe(b25.isSelected());
    }//GEN-LAST:event_b25ActionPerformed

    private void b26ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b26ActionPerformed
        atualizaQtdEquipe(b26.isSelected());
    }//GEN-LAST:event_b26ActionPerformed

    private void b27ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b27ActionPerformed
        atualizaQtdEquipe(b27.isSelected());
    }//GEN-LAST:event_b27ActionPerformed

    private void b28ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b28ActionPerformed
        atualizaQtdEquipe(b28.isSelected());
    }//GEN-LAST:event_b28ActionPerformed

    private void b29ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b29ActionPerformed
        atualizaQtdEquipe(b29.isSelected());
    }//GEN-LAST:event_b29ActionPerformed

    private void b30ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b30ActionPerformed
        atualizaQtdEquipe(b30.isSelected());
    }//GEN-LAST:event_b30ActionPerformed

    private void b31ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b31ActionPerformed
        atualizaQtdEquipe(b31.isSelected());
    }//GEN-LAST:event_b31ActionPerformed

    private void b32ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b32ActionPerformed
        atualizaQtdEquipe(b32.isSelected());
    }//GEN-LAST:event_b32ActionPerformed

    private void b33ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b33ActionPerformed
        atualizaQtdEquipe(b33.isSelected());
    }//GEN-LAST:event_b33ActionPerformed

    private void b34ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b34ActionPerformed
        atualizaQtdEquipe(b34.isSelected());
    }//GEN-LAST:event_b34ActionPerformed

    private void b35ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b35ActionPerformed
        atualizaQtdEquipe(b35.isSelected());
    }//GEN-LAST:event_b35ActionPerformed

    private void b36ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_b36ActionPerformed
        atualizaQtdEquipe(b36.isSelected());
    }//GEN-LAST:event_b36ActionPerformed

    /**
     * @param args the command line arguments
     */

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JCheckBox b01;
    private javax.swing.JCheckBox b02;
    private javax.swing.JCheckBox b03;
    private javax.swing.JCheckBox b04;
    private javax.swing.JCheckBox b05;
    private javax.swing.JCheckBox b06;
    private javax.swing.JCheckBox b07;
    private javax.swing.JCheckBox b08;
    private javax.swing.JCheckBox b09;
    private javax.swing.JCheckBox b10;
    private javax.swing.JCheckBox b11;
    private javax.swing.JCheckBox b12;
    private javax.swing.JCheckBox b13;
    private javax.swing.JCheckBox b14;
    private javax.swing.JCheckBox b15;
    private javax.swing.JCheckBox b16;
    private javax.swing.JCheckBox b17;
    private javax.swing.JCheckBox b18;
    private javax.swing.JCheckBox b19;
    private javax.swing.JCheckBox b20;
    private javax.swing.JCheckBox b21;
    private javax.swing.JCheckBox b22;
    private javax.swing.JCheckBox b23;
    private javax.swing.JCheckBox b24;
    private javax.swing.JCheckBox b25;
    private javax.swing.JCheckBox b26;
    private javax.swing.JCheckBox b27;
    private javax.swing.JCheckBox b28;
    private javax.swing.JCheckBox b29;
    private javax.swing.JCheckBox b30;
    private javax.swing.JCheckBox b31;
    private javax.swing.JCheckBox b32;
    private javax.swing.JCheckBox b33;
    private javax.swing.JCheckBox b34;
    private javax.swing.JCheckBox b35;
    private javax.swing.JCheckBox b36;
    private javax.swing.JButton btnGravar;
    private javax.swing.JButton jButton1;
    private javax.swing.JButton jButton2;
    private javax.swing.JButton jButton3;
    private javax.swing.JButton jButton4;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel lbl01;
    private javax.swing.JLabel lbl02;
    private javax.swing.JLabel lbl03;
    private javax.swing.JLabel lbl04;
    private javax.swing.JLabel lbl05;
    private javax.swing.JLabel lbl06;
    private javax.swing.JLabel lbl07;
    private javax.swing.JLabel lbl08;
    private javax.swing.JLabel lbl09;
    private javax.swing.JLabel lbl10;
    private javax.swing.JLabel lbl11;
    private javax.swing.JLabel lbl12;
    private javax.swing.JLabel lbl13;
    private javax.swing.JLabel lbl14;
    private javax.swing.JLabel lbl15;
    private javax.swing.JLabel lbl16;
    private javax.swing.JLabel lbl17;
    private javax.swing.JLabel lbl18;
    private javax.swing.JLabel lbl19;
    private javax.swing.JLabel lbl20;
    private javax.swing.JLabel lbl21;
    private javax.swing.JLabel lbl22;
    private javax.swing.JLabel lbl23;
    private javax.swing.JLabel lbl24;
    private javax.swing.JLabel lbl25;
    private javax.swing.JLabel lbl26;
    private javax.swing.JLabel lbl27;
    private javax.swing.JLabel lbl28;
    private javax.swing.JLabel lbl29;
    private javax.swing.JLabel lbl30;
    private javax.swing.JLabel lbl31;
    private javax.swing.JLabel lbl32;
    private javax.swing.JLabel lbl33;
    private javax.swing.JLabel lbl34;
    private javax.swing.JLabel lbl35;
    private javax.swing.JLabel lbl37;
    private javax.swing.JLabel lblAviso;
    private javax.swing.JLabel lblQuantidade;
    // End of variables declaration//GEN-END:variables
}
