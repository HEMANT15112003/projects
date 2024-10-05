import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

class BankAccount {
    private double balance;

    // Constructor to initialize balance
    public BankAccount(double initialDeposit) {
        this.balance = initialDeposit;
    }

    // Method to deposit money
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    // Method to withdraw money
    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        } else {
            return false;
        }
    }

    // Method to check balance
    public double getBalance() {
        return balance;
    }
}

public class BankingSystemGUI extends JFrame implements ActionListener {

    private BankAccount account;
    private JLabel balanceLabel;
    private JTextField amountField;
    private JButton depositButton, withdrawButton;

    public BankingSystemGUI() {
        account = new BankAccount(0);  // Initialize with zero balance

        // GUI setup
        setTitle("Banking System");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(3, 2));

        // Labels and text fields
        JLabel amountLabel = new JLabel("Enter Amount:");
        amountField = new JTextField();
        balanceLabel = new JLabel("Balance: $0.00");

        // Buttons
        depositButton = new JButton("Deposit");
        withdrawButton = new JButton("Withdraw");

        // Adding action listeners to buttons
        depositButton.addActionListener(this);
        withdrawButton.addActionListener(this);

        // Adding components to the frame
        add(amountLabel);
        add(amountField);
        add(depositButton);
        add(withdrawButton);
        add(balanceLabel);

        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        double amount = 0;
        try {
            amount = Double.parseDouble(amountField.getText());
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "Please enter a valid number.");
            return;
        }

        if (e.getSource() == depositButton) {
            account.deposit(amount);
            JOptionPane.showMessageDialog(this, "Deposit Successful!");
            updateBalanceLabel();
        } else if (e.getSource() == withdrawButton) {
            if (account.withdraw(amount)) {
                JOptionPane.showMessageDialog(this, "Withdrawal Successful!");
            } else {
                JOptionPane.showMessageDialog(this, "Insufficient Balance.");
            }
            updateBalanceLabel();
        }

        // Clear the input field after action
        amountField.setText("");
    }

    // Method to update the balance label
    private void updateBalanceLabel() {
        balanceLabel.setText("Balance: $" + String.format("%.2f", account.getBalance()));
    }

    public static void main(String[] args) {
        new BankingSystemGUI();
    }
}
