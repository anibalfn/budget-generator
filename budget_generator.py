#!/usr/bin/env python
# coding: utf-8

# In[ ]:


project_description = input("Type the project description: ");
estimated_hours = input("Type estimated hours to finish the project: ");
hour_price = input("Type the value per worked hour: ");
estimated_time = input("Type the estimated deadline: ");


# In[ ]:


estimated_value_total = int(estimated_hours) * int(hour_price);
print(estimated_value_total);


# In[ ]:


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


# In[ ]:


pdf.output("budget.pdf");
print("Budget generated with success.");

