from ultralytics import YOLO

def detect_components(image_path):
    model = YOLO('../runs/detect/modelo-arquitetura/weights/best.pt')
    results = model.predict(image_path, conf=0.3)

    components = []
    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            component = result.names[cls_id]
            components.append(component)

    return list(set(components))

def generate_stride_report(components):
    STRIDE_MAPPING = {
        "API": ["Spoofing", "Tampering", "Information Disclosure", "Denial of Service"],
        "Aplicação": ["Tampering", "Repudiation", "Information Disclosure", "Denial of Service", "Elevation of Privilege"],
        "Banco de Dados": ["Tampering", "Information Disclosure", "Denial of Service", "Elevation of Privilege"],
        "Servidores": ["Spoofing", "Tampering", "Denial of Service", "Elevation of Privilege"],
        "Usuarios": ["Spoofing", "Repudiation", "Elevation of Privilege"]
    }

    stride_report = {}
    for component in components:
        threats = STRIDE_MAPPING.get(component, [])
        stride_report[component] = threats

    return stride_report

def get_vulnerabilities(component, threats):
    VULNERABILITIES_DB = {
        "API": {
            "Spoofing": {
                "vulnerabilidades": ["Token JWT fraco", "Ausência de MFA", "Roubo de credenciais", "Falhas OAuth"],
                "contramedidas": ["JWT robusto", "Implementar MFA", "OAuth seguro", "Proteção contra brute-force"]
            },
            "Tampering": {
                "vulnerabilidades": ["Manipulação de Payload", "Injeção SQL", "Ataques de desserialização"],
                "contramedidas": ["Validação robusta", "Prepared Statements", "Sanitização dos dados"]
            },
            "Information Disclosure": {
                "vulnerabilidades": ["Exposição de dados sensíveis", "Logs expostos", "Mensagens de erro detalhadas"],
                "contramedidas": ["Ofuscação de dados sensíveis", "Criptografia dos logs", "Tratamento seguro de erros"]
            },
            "Denial of Service": {
                "vulnerabilidades": ["Throttling ineficiente", "Recursos mal dimensionados"],
                "contramedidas": ["Rate limiting", "Escalabilidade automática"]
            }
        },

        "Banco de Dados": {
            "Tampering": {
                "vulnerabilidades": ["Injeção SQL", "Acesso não autorizado", "Manipulação direta dos dados"],
                "contramedidas": ["Prepared Statements", "Controle rígido de acessos",
                                  "Auditoria e monitoramento contínuo"]
            },
            "Information Disclosure": {
                "vulnerabilidades": ["Dados não criptografados", "Backups expostos", "Configuração inadequada"],
                "contramedidas": ["Criptografia em repouso", "Backups seguros", "Hardening do banco de dados"]
            },
            "Denial of Service": {
                "vulnerabilidades": ["Queries lentas", "Configurações inadequadas"],
                "contramedidas": ["Otimização de queries", "Monitoramento contínuo", "Políticas de timeout"]
            },
            "Elevation of Privilege": {
                "vulnerabilidades": ["Falhas nas permissões de usuário", "Privilégios excessivos"],
                "contramedidas": ["Privilégio mínimo", "Controle de acessos baseado em função (RBAC)"]
            }
        },

        "Aplicação": {
            "Tampering": {
                "vulnerabilidades": ["Cross-Site Scripting (XSS)", "Cross-Site Request Forgery (CSRF)",
                                     "Falhas de validação"],
                "contramedidas": ["Sanitização de entradas", "Anti-CSRF tokens", "Validação rigorosa"]
            },
            "Repudiation": {
                "vulnerabilidades": ["Ausência de logs adequados", "Logs não confiáveis"],
                "contramedidas": ["Auditoria robusta", "Logs com integridade garantida"]
            },
            "Information Disclosure": {
                "vulnerabilidades": ["Erro detalhado", "Logs expostos", "Headers inseguros"],
                "contramedidas": ["Tratamento genérico de erros", "Proteção de logs", "Hardening de headers"]
            },
            "Denial of Service": {
                "vulnerabilidades": ["Processamento ineficiente", "Falta de proteção contra ataques DoS"],
                "contramedidas": ["Rate limiting", "Proteção DoS (ex: CDN)"]
            },
            "Elevation of Privilege": {
                "vulnerabilidades": ["Falhas de autenticação/autorização", "Insegurança no controle de acesso"],
                "contramedidas": ["RBAC", "Controle rigoroso de sessão", "Autenticação robusta"]
            }
        },

        "Servidores": {
            "Spoofing": {
                "vulnerabilidades": ["IP Spoofing", "Roubo de credenciais de acesso"],
                "contramedidas": ["Firewall eficaz", "IDS/IPS", "Autenticação forte"]
            },
            "Tampering": {
                "vulnerabilidades": ["Alteração indevida de configurações", "Falta de monitoramento"],
                "contramedidas": ["Monitoramento ativo", "Controle rigoroso de acesso"]
            },
            "Denial of Service": {
                "vulnerabilidades": ["Ataques DDoS", "Configuração inadequada dos recursos"],
                "contramedidas": ["Mitigação DDoS", "Balanceamento de carga", "Alta disponibilidade"]
            },
            "Elevation of Privilege": {
                "vulnerabilidades": ["Acesso administrativo indevido", "Falhas em políticas de segurança"],
                "contramedidas": ["Políticas de privilégio mínimo", "Hardening do servidor", "Auditorias regulares"]
            }
        },

        "Usuarios": {
            "Spoofing": {
                "vulnerabilidades": ["Phishing", "Engenharia social", "Roubo de senhas"],
                "contramedidas": ["Campanhas de conscientização", "MFA", "Gerenciadores de senhas"]
            },
            "Repudiation": {
                "vulnerabilidades": ["Ausência de auditoria", "Registro inadequado das ações"],
                "contramedidas": ["Auditoria eficaz", "Registro imutável das ações"]
            },
            "Elevation of Privilege": {
                "vulnerabilidades": ["Acesso a áreas restritas", "Contas com privilégio excessivo"],
                "contramedidas": ["Revisão periódica de permissões", "RBAC", "Auditorias regulares"]
            }
        }
    }

    details = {}
    for threat in threats:
        vuln_data = VULNERABILITIES_DB.get(component, {}).get(threat, {})
        if vuln_data:
            details[threat] = vuln_data

    return details

