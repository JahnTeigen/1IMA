namespace UserData
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            btnRegister = new Button();
            txtbUsername = new TextBox();
            txtbPassword = new TextBox();
            SuspendLayout();
            // 
            // btnRegister
            // 
            btnRegister.Location = new Point(12, 71);
            btnRegister.Name = "btnRegister";
            btnRegister.Size = new Size(100, 26);
            btnRegister.TabIndex = 0;
            btnRegister.Text = "button1";
            btnRegister.UseVisualStyleBackColor = true;
            btnRegister.Click += btnRegister_Click;
            // 
            // txtbUsername
            // 
            txtbUsername.Location = new Point(12, 12);
            txtbUsername.Name = "txtbUsername";
            txtbUsername.Size = new Size(100, 23);
            txtbUsername.TabIndex = 1;
            txtbUsername.TextChanged += txtbUsername_TextChanged;
            // 
            // txtbPassword
            // 
            txtbPassword.Location = new Point(12, 41);
            txtbPassword.Name = "txtbPassword";
            txtbPassword.Size = new Size(100, 23);
            txtbPassword.TabIndex = 1;
            txtbPassword.TextChanged += txtbPassword_TextChanged;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(625, 378);
            Controls.Add(txtbPassword);
            Controls.Add(txtbUsername);
            Controls.Add(btnRegister);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button btnRegister;
        private TextBox txtbUsername;
        private TextBox txtbPassword;
    }
}
