/* Fix for Test Case 1 */
int read_gift_card(unsigned char *buf, int bufSize)
{
    int i;
    for (i = 0; i < bufSize; i++)
    {
        buf[i] = getchar();
        if (buf[i] == '\n')
        {
            buf[i] = '\0'; // Null-terminate the buffer
            break;
        }
    }
    return i; // Return the number of characters read
}


/* Fix for Test Case 2 */
int read_gift_card(unsigned char *buf, int bufSize)
{
    int i;
    for (i = 0; i < bufSize; i++)
    {
        int c = getchar();
        if (c == '\n' || c == EOF) // Exit loop if newline or end of file is reached
        {
            buf[i] = '\0'; // Null-terminate the buffer
            break;
        }
        buf[i] = c;
    }
    return i; // Return the number of characters read
}


/* Fix for Test Case 3 */
int read_gift_card(unsigned char *buf, int bufSize)
{
    int i;
    for (i = 0; i < bufSize-1; i++)
    {
        int c = getchar();
        if (c == '\n' || c == EOF) // Exit loop if newline or end of file is reached
        {
            break;
        }
        buf[i] = c;
    }
    buf[i] = '\0'; // Null-terminate the buffer
    return i; // Return the number of characters read
}
