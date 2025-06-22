using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace anuragwinapp
{
    public partial class Form11 : Form
    {
        private object textBoxName;
        private object textBoxRoll;

        public Form11()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string student = "Name: " + textBox1.Text +
                             ", Roll: " + textBox2.Text +
                             ", Mail: " + textBox3.Text +
                             ", Phone: " + textBox4.Text +
                             ", Gender: " + textBox5.Text +
                             ", Address: " + textBox6.Text;
                               listBox1.Items.Add(student);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedIndex >= 0)
            {
                listBox1.Items.RemoveAt(listBox1.SelectedIndex);
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            textBox1.Clear();
            textBox2.Clear();
            textBox3.Clear();
            textBox4.Clear();
            textBox5.Clear();
            textBox6.Clear();
            
        }

        private void button4_Click(object sender, EventArgs e)
        {
            this.Close();

        }
    }
}
