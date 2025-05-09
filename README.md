<h1 align="center"> Desafio Sistema Bancário com Python – Versão 2 </h1>

Este projeto é uma simulação de um sistema bancário simples, desenvolvido com o objetivo de praticar e aplicar os conceitos de modularização de código, organização de funções e manipulação de dados em Python.

## Tecnologia utilizada

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

## Desafio

Para tornar o código mais modularizado e organizado:

    Criar funções separadas para as operações: sacar, depositar e extrato.

    Adicionar duas novas funções:

        criar_usuario(): responsável pelo cadastro de clientes.

        criar_conta_corrente(): responsável por vincular uma conta a um usuário existente.

## Objetivo Geral

Refatorar um sistema bancário básico, separando as operações de saque, depósito e extrato em funções específicas. Além disso, implementar novas funcionalidades para cadastro de usuários (clientes) e contas bancárias, de forma organizada e reutilizável.

## Objetivos Específicos

### Operação de Depósito:

A função depositar() deve receber os argumentos por posição apenas (positional-only arguments).

Só permite depósitos com valores positivos.

### Operação de Sacar:

A função sacar() deve obrigatoriamente receber seus argumentos por nome (keyword-only arguments).

### Operação de Visualizar Extrato:

A função mostrar_extrato() deve receber argumentos por posição e nome, combinando positional-only e keyword-only.

### Operação de Criar Usuário:

Os usuários são armazenados em uma lista.

Cada usuário contém:

    Nome completo

    Data de nascimento

    CPF (somente números)

    Endereço (no formato: logradouro, número - bairro - cidade/UF)

Não é permitido cadastrar dois usuários com o mesmo CPF.

### Operação de Criar Conta Corrente:

As contas também são armazenadas em uma lista.

Cada conta contém:

    Número da conta (sequencial, iniciando em 1)

    Agência (fixa: 0001)

    Referência ao usuário dono da conta

Um usuário pode ter várias contas, mas cada conta pertence a apenas um usuário.


