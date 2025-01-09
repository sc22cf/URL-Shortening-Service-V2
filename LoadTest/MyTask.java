class ClientHandler implements Runnable {
    private final Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {
        System.out.println("Server is running and waiting for a connection...");
        Socket socket = serverSocket.accept(); // Accept one client
        System.out.println("Client connected: " + socket.getInetAddress());

        // Handle client communication
        BufferedReader input = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        PrintWriter output = new PrintWriter(socket.getOutputStream(), true);

        String message;
        while ((message = input.readLine()) != null) {
            System.out.println("Received: " + message);
            output.println("Echo: " + message); // Echo back to client
        }   
    }
}

public class MultithreadingExample {
    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(12345)) {
            while (true){
                Socket clientSocket = serverSocket.accept();
                Thread clientThread = new Thread(new ClientHandler(clientSocket));
                clientThread.start();
            }
        }
        catch (IOException e){
            e.printStackTrace();
        }
    }
}
