using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1
{

    public partial class Form1 : Form
    {

        private string username = "freddy";
        private string password = "Freddy123";

        public Form1()

        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void button1_ButtonClicked(object sender, EventArgs e)
        {
            if (textBox1.Text == username && textBox2.Text == password)
            {
                Console.WriteLine("Username & password correct");
            }
            else
            {
                Console.WriteLine("Wrong input");
            }
        }

        private void label1_Click(object sender, EventArgs e)
        {
            
        }
    }
}
