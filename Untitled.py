#!/usr/bin/env python
# coding: utf-8

# In[1]:


project_description = input("Digite a descrição do projeto: ");
estimated_hours = input("Digite a estimativa de horas para conclusão: ");
hour_price = input("Digite o valor da hora trabalhada: ");
estimated_time = input("Digite o prazo estimado: ");


# In[2]:


estimated_value_total = int(estimated_hours) * int(hour_price);
print(estimated_value_total);


# In[6]:


from fpdf import FPDF;

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")
pdf.image("template.png", x=0, y=0);

pdf.text(115, 145, project_description);
pdf.text(115, 160, estimated_hours);
pdf.text(115, 175, hour_price);
pdf.text(115, 190, estimated_time);
pdf.text(115, 205, str(estimated_value_total));


# In[7]:


pdf.output("orçamento.pdf");
print("Orçamento gerado com sucesso.");

