﻿/*Задача 51: Задайте двумерный массив. Найдите сумму 
элементов, находящихся на главной диагонали (с индексами 
(0,0); (1;1) и т.д.
Например, задан массив:
1 4 7 2
5 9 2 3
8 4 2 4
Сумма элементов главной диагонали: 1+9+2 = 12*/

int[,] CreateMatrixRndInt(int rows, int columns, int min, int max)
{
    int[,] matrix = new int[rows,columns];
    Random rnd = new Random();

    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            matrix[i, j] = rnd.Next(min, max + 1);
        }
    }
    return matrix; 
}

void PrintMatrix (int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            Console.Write($"{matrix[i, j], 4}");
        }
        Console.WriteLine("");
    }
}

int FindSumDiagonalDigit(int[,] matrix)
{
    int diagonalDigitSum = 0;
    for (int i = 0; i < matrix.GetLength(0) 
        && i < matrix.GetLength(1); i++)
    {
        int j = i;
        diagonalDigitSum = diagonalDigitSum + matrix[i, j];
    }
    return diagonalDigitSum;
}

void PrintFindSumDiagonalDigit(int[,] matrix, int sum)
{
    Console.Write("Сумма элементов главной диагонали: ");
    for (int i = 0; i < matrix.GetLength(0) 
        && i < matrix.GetLength(1); i++)
    {
        int j = i;
        Console.Write($"{matrix[i, j]} ");
        if (i + 1 < matrix.GetLength(0)
            && i + 1 < matrix.GetLength(1))
        {
            Console.Write("+ ");
        }
        else
        {
            Console.Write($"= {sum}");
        }
    }
}





int[,] array2d = CreateMatrixRndInt(3, 4, 0, 10);
PrintMatrix(array2d);
int diagonalDigitSum = FindSumDiagonalDigit(array2d);
PrintFindSumDiagonalDigit(array2d, diagonalDigitSum);