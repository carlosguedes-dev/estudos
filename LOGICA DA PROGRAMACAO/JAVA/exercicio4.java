import java.util.Scanner;

public class exercicio4{

    public int[] numeros = {10,20,30};
    //criando um sistema de pontuacao de um jogo em java
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        int pontos = 0;
        System.out.println("Bem-vindo! Pressione S para continuar");
        String string = scanner.nextLine();
        if(string.equalsIgnoreCase("s")) {
            System.out.println("Qual é a capital do Brasil?");
            string = scanner.nextLine();
            if(string.equalsIgnoreCase("Brasilia")) {
                pontos++;
                System.out.println("Resposta correta! Voce pontuou");
                System.out.println("Voce deseja continuar? (s/n)");
                string = scanner.nextLine();
                if(string.equalsIgnoreCase("s")) {
                    //PROXIMA PERGUNTA
                    System.out.println("Em qual continente fica o Brasil?");
                    string = scanner.nextLine();
                    if(string.equals("america do sul")) {
                        pontos++;
                        System.out.println("Resposta correta! Voce pontuou");
                        System.out.println("Voce deseja continuar? (s/n)");
                        string = scanner.nextLine();
                        if(string.equalsIgnoreCase("s")) {
                            System.out.println("Qual é a moeda do Brasil?");
                            string = scanner.nextLine();
                            if(string.equals("real")) {
                                pontos++;
                                System.out.println("Resposta correta! Voce pontuou");
                                System.out.println("Acabou o jogo... Voce pontoou " +pontos);
                            }
                            else {
                                System.out.println("Resposta incorreta! Sua pontuação foi de: " +pontos);
                            }
                        }else {
                            System.out.println("Acabou o jogo... Voce pontoou " +pontos);
                        }
                        
                    }else {
                        System.out.println("Resposta incorreta! Sua pontuação foi de: " + pontos);
                    }
                } else {
                    System.out.println("Acabou o jogo... Voce pontoou " + pontos);
                }
            }else {
                System.out.println("Resposta incorreta! Sua pontuação foi de: " +pontos);
            }
        }else {
            System.out.println("Acabou o jogo... Voce pontoou 0");
        }
    }
}