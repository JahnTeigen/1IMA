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

                    // SQL query with positional parameters
                    string query = "INSERT INTO UserData ([firstname], [surname], [admin], [password]) VALUES (?, ?, ?, ?)";
                    using (OleDbCommand command = new OleDbCommand(query, connection))
                    {
                        // Add parameters in the order they appear in the SQL query
                        command.Parameters.AddWithValue("?", txtbUsername.Text); // Username/firstname
                        command.Parameters.AddWithValue("?", txtbSurname.Text); // Surname
                        command.Parameters.AddWithValue("?", false);
                        command.Parameters.AddWithValue("?", txtbPassword.Text); // Password

                        txtbUsername.Text = "";
                        txtbSurname.Text = "";
                        txtbPassword.Text = "";
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
                catch (OleDbException ex)
                {
                    MessageBox.Show("A database error occurred: " + ex.Message);
                }
                catch (Exception ex)
                {
                    MessageBox.Show("An error occurred: " + ex.Message);
                }
                finally
                {
                    connection.Close();
                }
            }

        }

        private void txtbUsername_TextChanged(object sender, EventArgs e)
        {

        }

        private void txtbPassword_TextChanged(object sender, EventArgs e)
        {

        }

        private void splitContainer1_Panel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void splitContainer1_Panel2_Paint(object sender, PaintEventArgs e)
        {

        }
    }
}
