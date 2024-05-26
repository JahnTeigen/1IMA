using System.Data.OleDb;
using System.Data;
using System.Windows.Forms;

namespace UserData
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnRegister_Click(object sender, EventArgs e)
        {
            string connectionString = @"Provider=Microsoft.ACE.OLEDB.12.0;Data Source=E:\VStudio\Projects\UserData\UserData\UserDatabase.accdb;";
            using (OleDbConnection connection = new OleDbConnection(connectionString))
            {
                try
                {
                    connection.Open();
                    string query = "INSERT INTO UserData (username, password) VALUES (@username, @password)";
                    using (OleDbCommand command = new OleDbCommand(query, connection))
                    {
                        command.Parameters.AddWithValue("@username", txtbUsername.Text);
                        command.Parameters.AddWithValue("@password", txtbPassword.Text);
                        int result = command.ExecuteNonQuery();

                        if (result > 0)
                        {
                            MessageBox.Show("User registered successfully.");
                        }
                        else
                        {
                            MessageBox.Show("User registration failed.");
                        }
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show("An error occurred: " + ex.Message);
                }
            }
        }

        private void txtbUsername_TextChanged(object sender, EventArgs e)
        {

        }

        private void txtbPassword_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
