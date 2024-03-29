﻿//Задача 39:
//Напишите программу, которая перевернет одномерный массив
//(последний элемент будет на первом месте, а первый - на последнем)
//[4 2 3 4 5] -> [5 4 3 2 1]
//[6 7 3 6] -> [6 3 7 6]


int[] CreateArray(int size, int min, int max)
{
    int[] arr = new int[size];
    Random rnd = new Random();

    for (int i = 0; i < size; i++)
    {
        arr[i] = rnd.Next(min, max + 1);
    }
    return arr;
}

void PrintArray(int[] arr)
{
    Console.Write("[");
    for (int i = 0; i < arr.Length; i++)
    {
        Console.Write(arr[i]);
        if (i < arr.Length - 1) Console.Write(", ");
    }
    
    Console.Write("]");
}

void ReverseArray (int[] arr)
{
    int temp = 0;
    for (int i = 0; i < arr.Length / 2; i++)
    {
        temp = arr[i];
        arr[i] = arr[arr.Length - 1 - i];
        arr[arr.Length - 1 - i] = temp;
    }
}

int[] array = CreateArray(5, 0, 10);
PrintArray(array);
Console.Write(" -> ");
ReverseArray(array);
PrintArray(array);