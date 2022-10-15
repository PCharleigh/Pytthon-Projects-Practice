text = """In 1791, U.S. Secretary of the Treasury Alexander Hamilton began a romantic affair with Maria Reynolds. Both were married at the time.

Maria’s husband, James Reynolds, soon discovered the affair. Rather than try to stop it, he decided to profit from the situation by extorting money from Hamilton in exchange for keeping quiet. Maria likely hatched the blackmail scheme with her husband.

In 1792, when James Reynolds was imprisoned on forgery charges, Hamilton refused to help him. In retaliation, Reynolds not only shared details of the affair with Hamilton’s political adversaries, the Republicans, he also implicated Hamilton in a financial speculation scheme. Hamilton had not been involved in the speculation scheme and, indeed, knew nothing about it before Reynolds’s charge.

Years later, when the charge resurfaced, Hamilton worried about the reputation of the U.S. Treasury and the future of his Federalist Party.  He believed that by publicly admitting his affair with Maria Reynolds, it would be clear that he had nothing to hide, and that none of the other accusations were true. To that end, he published this pamphlet, the appendix of which contains the content of letters received from Maria (signed “Mari”) Reynolds, James Reynolds, and others. """


# print(len(text.split()))

word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)